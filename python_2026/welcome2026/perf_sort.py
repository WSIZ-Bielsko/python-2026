from random import randint

from python_2026.common import ts, duration


def gen_sample(n_elems=10 ** 3) -> list[int]:
    return [randint(1, 10 ** 9) for _ in range(n_elems)]


def task(exp: int):
    data = gen_sample(2 ** exp)
    st = ts()
    data.sort()
    print(f'size={2 ** exp:10} time={duration(st)}')


if __name__ == '__main__':
    # w = gen_sample(20)
    for i in range(15, 24):
        task(i)
