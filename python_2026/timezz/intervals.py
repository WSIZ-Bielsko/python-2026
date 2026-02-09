from datetime import datetime, UTC


def do_intervals_overlap(startts1, endts1, startts2, endts2) -> bool:
    for dt in [startts1, endts1, startts2, endts2]:
        if not isinstance(dt, datetime) or dt.tzinfo is None:
            raise ValueError("All arguments must be timezone-aware datetimes")

    start1 = startts1.astimezone(UTC)
    end1 = endts1.astimezone(UTC)
    start2 = startts2.astimezone(UTC)
    end2 = endts2.astimezone(UTC)

    if start2 < start1:
        s1, t1 = start1, end1
        start1, end1 = start2, end2
        start2, end2 = s1, t1

    # start1 <= start2 is guaranteed

    return start2 < end1


if __name__ == '__main__':
    do_intervals_overlap(1, 2, 3, 4)


