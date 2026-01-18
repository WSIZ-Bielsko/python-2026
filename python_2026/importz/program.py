import os
from math import sin

from python_2026.importz.repo import save_str_to_file
from python_2026.importz.utils import ts




def foo():
    st = ts()

    n = 10 ** 6
    x = 0
    for i in range(n):
        x += sin(0.1 * i)

    en = ts()
    msg = f'duration: {en - st: .3f}'
    print(msg)
    print(f'cwd={os.getcwd()}')
    os.chdir("..")
    print(f'cwd={os.getcwd()}')
    save_str_to_file(file_name='result.txt', content=msg)




if __name__ == '__main__':
    foo()
