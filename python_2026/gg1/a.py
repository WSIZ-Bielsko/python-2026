from random import randint, seed

if __name__ == '__main__':
    seed(42)
    for _ in range(10):
        print(randint(0, 10))
