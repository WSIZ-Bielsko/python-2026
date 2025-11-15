def foo(arg1: str, arg2: str = 'kadabra', arg3='abra') -> list[str]:
    # ↑↑ domyślne wartości
    return arg1, arg2


if __name__ == '__main__':
    z = foo('a', 'b', 'c')
    z = foo('a')  # defaulty dla pozostałych
    z = foo(arg3='a', arg2='b', arg1='c')
