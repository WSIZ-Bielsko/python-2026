import math

from python_2026.gg1.utils import ts, duration


def get_sin(degree: float) -> float:
    return math.sin(degree * math.pi / 180)


if __name__ == '__main__':
    x = 0
    st = ts()
    for i in range(10 ** 6):
        x += get_sin(i)

    print(f'duration: {duration(st):.6f}')