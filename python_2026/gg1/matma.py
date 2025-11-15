import math
from datetime import datetime


def ts() -> float:
    return datetime.now().timestamp()


def duration(start_ts) -> float:
    return ts() - start_ts

def get_sin(degree: float) -> float:
    return math.sin(degree * math.pi / 180)


if __name__ == '__main__':
    x = 0
    st = ts()
    for i in range(10 ** 6):
        x += get_sin(i)

    print(f'duration: {duration(st):.6f}')