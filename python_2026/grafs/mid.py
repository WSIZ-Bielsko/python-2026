from python_2026.grafs.basics import generate_random_graph, gen_len_list

if __name__ == '__main__':
    # graph = generate_random_graph(n=10, mi_edges=2, mx_edges=5)
    # for k,v in graph.items():
    #     print(k, v)
    # print(can_reach(graph, 1, 10))

    aavg = 1.2
    for i in range(10):
        ll = gen_len_list(n=100, mi=1, mx=5, avg=aavg)
        r_avg = sum(ll) / len(ll)
        print(f'{i}: {r_avg:.2f}, {aavg:.2f}')
