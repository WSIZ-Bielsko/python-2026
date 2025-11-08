from datetime import datetime
from time import sleep


def ts() -> float:
    return datetime.now().timestamp()


def duration(start_ts) -> float:
    return ts() - start_ts


if __name__ == '__main__':
    st = ts()
    sleep(0.1)
    print(duration(st))