import pytest
from datetime import datetime, timezone, timedelta

from python_2026.timezz.intervals import do_intervals_overlap


def test_complete_overlap():
    """Interval 2 completely inside interval 1"""
    start1 = datetime(2026, 1, 1, 10, 0, tzinfo=timezone.utc)
    end1 = datetime(2026, 1, 1, 14, 0, tzinfo=timezone.utc)
    start2 = datetime(2026, 1, 1, 11, 0, tzinfo=timezone.utc)
    end2 = datetime(2026, 1, 1, 13, 0, tzinfo=timezone.utc)
    assert do_intervals_overlap(start1, end1, start2, end2) is True

def test_partial_overlap():
    """Intervals partially overlap"""
    start1 = datetime(2026, 1, 1, 10, 0, tzinfo=timezone.utc)
    end1 = datetime(2026, 1, 1, 12, 0, tzinfo=timezone.utc)
    start2 = datetime(2026, 1, 1, 11, 0, tzinfo=timezone.utc)
    end2 = datetime(2026, 1, 1, 13, 0, tzinfo=timezone.utc)
    assert do_intervals_overlap(start1, end1, start2, end2) is True

def test_no_overlap_before():
    """Interval 2 completely before interval 1"""
    start1 = datetime(2026, 1, 1, 12, 0, tzinfo=timezone.utc)
    end1 = datetime(2026, 1, 1, 14, 0, tzinfo=timezone.utc)
    start2 = datetime(2026, 1, 1, 8, 0, tzinfo=timezone.utc)
    end2 = datetime(2026, 1, 1, 10, 0, tzinfo=timezone.utc)
    assert do_intervals_overlap(start1, end1, start2, end2) is False

def test_no_overlap_after():
    """Interval 2 completely after interval 1"""
    start1 = datetime(2026, 1, 1, 8, 0, tzinfo=timezone.utc)
    end1 = datetime(2026, 1, 1, 10, 0, tzinfo=timezone.utc)
    start2 = datetime(2026, 1, 1, 12, 0, tzinfo=timezone.utc)
    end2 = datetime(2026, 1, 1, 14, 0, tzinfo=timezone.utc)
    assert do_intervals_overlap(start1, end1, start2, end2) is False

def test_edge_touching():
    """Intervals touch at boundary (end1 == start2)"""
    start1 = datetime(2026, 1, 1, 10, 0, tzinfo=timezone.utc)
    end1 = datetime(2026, 1, 1, 12, 0, tzinfo=timezone.utc)
    start2 = datetime(2026, 1, 1, 12, 0, tzinfo=timezone.utc)
    end2 = datetime(2026, 1, 1, 14, 0, tzinfo=timezone.utc)
    assert do_intervals_overlap(start1, end1, start2, end2) is False

def test_different_timezones():
    """Intervals in different timezones that overlap"""
    utc_plus_2 = timezone(timedelta(hours=2))
    utc_minus_5 = timezone(timedelta(hours=-5))
    start1 = datetime(2026, 1, 1, 12, 0, tzinfo=timezone.utc)  # 12:00 UTC
    end1 = datetime(2026, 1, 1, 14, 0, tzinfo=timezone.utc)    # 14:00 UTC
    start2 = datetime(2026, 1, 1, 15, 0, tzinfo=utc_plus_2)    # 13:00 UTC
    end2 = datetime(2026, 1, 1, 11, 0, tzinfo=utc_minus_5)     # 16:00 UTC
    assert do_intervals_overlap(start1, end1, start2, end2) is True

def test_different_timezones_no_overlap():
    """Intervals in different timezones that don't overlap"""
    utc_plus_3 = timezone(timedelta(hours=3))
    start1 = datetime(2026, 1, 1, 10, 0, tzinfo=timezone.utc)  # 10:00 UTC
    end1 = datetime(2026, 1, 1, 11, 0, tzinfo=timezone.utc)    # 11:00 UTC
    start2 = datetime(2026, 1, 1, 15, 0, tzinfo=utc_plus_3)    # 12:00 UTC
    end2 = datetime(2026, 1, 1, 16, 0, tzinfo=utc_plus_3)      # 13:00 UTC
    assert do_intervals_overlap(start1, end1, start2, end2) is False

def test_identical_intervals():
    """Identical intervals in same timezone"""
    start1 = datetime(2026, 1, 1, 10, 0, tzinfo=timezone.utc)
    end1 = datetime(2026, 1, 1, 12, 0, tzinfo=timezone.utc)
    start2 = datetime(2026, 1, 1, 10, 0, tzinfo=timezone.utc)
    end2 = datetime(2026, 1, 1, 12, 0, tzinfo=timezone.utc)
    assert do_intervals_overlap(start1, end1, start2, end2) is True


import pytest
from datetime import datetime, timezone, timedelta


def test_shared_start_enclosure():
    """Intervals starting at the exact same time but one is shorter."""
    t_start = datetime(2026, 2, 1, 10, 0, tzinfo=timezone.utc)
    t_mid = datetime(2026, 2, 1, 11, 0, tzinfo=timezone.utc)
    t_end = datetime(2026, 2, 1, 12, 0, tzinfo=timezone.utc)

    # Interval 1: 10-12, Interval 2: 10-11
    assert do_intervals_overlap(t_start, t_end, t_start, t_mid) is True


def test_shared_end_enclosure():
    """Intervals ending at the exact same time."""
    t_start = datetime(2026, 2, 1, 10, 0, tzinfo=timezone.utc)
    t_mid = datetime(2026, 2, 1, 11, 0, tzinfo=timezone.utc)
    t_end = datetime(2026, 2, 1, 12, 0, tzinfo=timezone.utc)

    # Interval 1: 10-12, Interval 2: 11-12
    assert do_intervals_overlap(t_start, t_end, t_mid, t_end) is True


def test_microsecond_overlap():
    """Intervals overlap by exactly 1 microsecond."""
    t1 = datetime(2026, 2, 1, 10, 0, 0, 0, tzinfo=timezone.utc)
    t2 = datetime(2026, 2, 1, 11, 0, 0, 0, tzinfo=timezone.utc)

    # Interval 1 ends at 11:00:00.000000
    # Interval 2 starts at 10:59:59.999999
    t2_minus_1us = t2 - timedelta(microseconds=1)
    t3 = t2 + timedelta(hours=1)

    assert do_intervals_overlap(t1, t2, t2_minus_1us, t3) is True


def test_extreme_timezone_dateline():
    """Intervals crossing the dateline with extreme timezones (+14 and -12)."""
    # Kiribati (UTC+14) and Baker Island (UTC-12) have a 26-hour difference.
    tz_kiri = timezone(timedelta(hours=14))
    tz_baker = timezone(timedelta(hours=-12))

    # Jan 2, 10:00 AM in Kiri is Jan 1, 20:00 UTC
    start1 = datetime(2026, 1, 2, 10, 0, tzinfo=tz_kiri)
    end1 = datetime(2026, 1, 2, 12, 0, tzinfo=tz_kiri)  # Jan 1, 22:00 UTC

    # Jan 1, 09:00 AM in Baker is Jan 1, 21:00 UTC
    start2 = datetime(2026, 1, 1, 9, 0, tzinfo=tz_baker)
    end2 = datetime(2026, 1, 1, 11, 0, tzinfo=tz_baker)  # Jan 1, 23:00 UTC

    # Overlap is 21:00 UTC to 22:00 UTC
    assert do_intervals_overlap(start1, end1, start2, end2) is True
