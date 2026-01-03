from datetime import datetime


def ts():
    return datetime.now().timestamp()


def duration(start_ts):
    return f'{ts() - start_ts:.3f}s'
