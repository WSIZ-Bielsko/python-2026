import random
from collections import defaultdict


def can_reach_2_steps(g, visited, start, end) -> bool:
    print(f'entering {start}')
    if start == end:
        return True
    visited.add(start)
    for nxt in g[start]:
        if nxt not in visited and can_reach_2_steps(g, visited, nxt, end):
            return True
    return False


def gen_len_list(n, mi, mx, avg):
    # generate a list of n numbers, each at least mi and at most mx, with average avg
    res = [mi] * n
    ssum = sum(res)
    while ssum < avg * n:
        tgt = random.randint(0,n-1)
        if res[tgt] < mx:
            res[tgt] += 1
        ssum += 1
    return res





def generate_random_graph(n: int, mi_edges: int, mx_edges: int) -> dict[int, list[int]]:
    g: dict[int, list[int]] = defaultdict(lambda: [])
    # how to change it ... to have avg number of edges per node??

    for z in range(1, n + 1):
        to_len = random.randint(mi_edges, mx_edges)
        all_nodes = list(range(1, n + 1))
        random.shuffle(all_nodes)
        random.shuffle(all_nodes)
        g[z] =sorted(all_nodes[:to_len])
    return g


if __name__ == '__main__':
    # node/user ... id: int
    # adjacency info ... id1 -> id2

    g: dict[int, list[int]] = defaultdict(lambda: [])  # jak nie ma jakiegoś klucza, to zwraca []
    # g[2] = [3,4,5] oznacza, że można przejść z 2 bezpośrednio do 3,4,5

    g[1] = [2, 3]
    g[2] = [4, 12, 44]
    g[3] = [5]
    g[4] = [7]
    g[7] = [6, 8]
    for i in range(8, 101):
        g[i].append(i + 1)

    print(g)
    # ? czy można przejść z 1 do 5?
    # print(f'1->5: {can_reach_2_steps(g, set(), 1, 5)}')
    print(f'1->6: {can_reach_2_steps(g, set(), 1, 6)}')
    # print(f'1->100: {can_reach_2_steps(g, set(), 1, 100)}')
