import sys


def compare_memory(sizes):
    for size in sizes:
        # Dictionary
        d = {i: i for i in range(size)}
        dict_bytes = sys.getsizeof(d)

        # List
        lst = [i for i in range(size)]
        list_bytes = sys.getsizeof(lst)

        # Tuple
        tup = tuple(range(size))
        tuple_bytes = sys.getsizeof(tup)

        print(f"\n{size:,} elements:")
        print(f" Dict: {dict_bytes:,} bytes ({dict_bytes / size:.2f} bytes/elem)")
        print(f" List: {list_bytes:,} bytes ({list_bytes / size:.2f} bytes/elem)")
        print(f" Tuple: {tuple_bytes:,} bytes ({tuple_bytes / size:.2f} bytes/elem)")
        print(f" Dict/List ratio: {dict_bytes / list_bytes:.2f}x")

if __name__ == '__main__':
    sizes = [1_000_000, 2_000_000, 4_000_000, 8_000_000]
    compare_memory(sizes)
    # Expected: dicts use ~3-4x more memory than lists/tuples
