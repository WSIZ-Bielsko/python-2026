def dist(t):
    return 0.1 * t + 0.01 * t ** 2 / 2


def get_acc(max_t: float, dt=1) -> list[float]:
    x = 0
    v = 0
    t = 0

    res = []
    while t < max_t:
        nx = dist(t)
        nv = (nx - x) / dt
        a = (nv - v) / dt
        #
        res.append(a)
        x = nx
        v = nv
        t = t + dt

    print(f'{t=}, x={dist(t)}')
    return res


if __name__ == '__main__':
    acc = get_acc(max_t=10, dt=0.01)
    print(acc)
