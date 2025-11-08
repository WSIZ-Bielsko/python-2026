from random import randint

from python_2026.gg1.utils import ts, duration

if __name__ == '__main__':
    print('tu zaczyna się wykonanie programu')

    secret = randint(0, 10)

    x1 = 0
    start_ts = ts()
    moves = 0
    while True:
        s1 = input('suggest a number: ')
        if s1 == 'x':
            break
        x1 = int(s1)
        moves += 1
        if x1 == secret:
            print(f'You got it! The secret number was {secret}')
            break
        else:
            print('secret is <' if x1 > secret else 'secret is >')

    print('ok')
    exec_time = duration(start_ts)
    print(f'exec time: {exec_time}, moves: {moves}')

