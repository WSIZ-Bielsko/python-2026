import time


def benchmark_dict_insertion(sizes):
    results = {}
    for size in sizes:
        start = time.perf_counter()
        d = {}
        for i in range(size):
            d[i] = i * 2
        elapsed = time.perf_counter() - start
        results[size] = elapsed
        print(f"{size:,} elements: {elapsed:.4f}s ({size / elapsed:,.0f} ops/sec)")
    return results


if __name__ == '__main__':
    # Test with 1M, 2M, 4M, 8M elements
    sizes = [1_000_000, 2_000_000, 4_000_000, 8_000_000]
    benchmark_dict_insertion(sizes)
    # Expected: roughly linear scaling (2x elements ≈ 2x time)
