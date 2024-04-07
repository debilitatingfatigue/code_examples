# топологическая сортировка

from sys import setrecursionlimit
import threading

def topological_sort(n, adjacency_list, color):
    def dfs(v, color, ans):
        color[v] = 1
        check = 0
        for u in adjacency_list[v]:
            if color[u] == 0:
                check = dfs(u, color, ans)
            if color[u] == 1 or check == -1:
                return -1
        color[v] = 2
        ans.append(v + 1)

        return check
    
    ans = []
    for vertes in range(n):
        if color[vertes] == 0:
            if dfs(vertes, color, ans) == -1:
                print('-1')
                return
            
    ans.reverse()
    print(*ans)


def main():
    read_raw =  [
        '6 6',
        '1 2',
        '3 2',
        '4 2',
#         '2 4',
        '2 5',
        '6 5',
        '4 6',
    ]

    n, m = map(int, read_raw[0].split())

    adjacency_list = [[] for _ in range(n)]
    color = [0 for _ in range(n)]

    for row in read_raw[1:]:
        v1, v2 = map(int, row.split())
        if v2 - 1 not in adjacency_list[v1 - 1]:
            adjacency_list[v1 - 1].append(v2 - 1)
    topological_sort(n, adjacency_list, color)


setrecursionlimit(10 ** 9)
threading.stack_size(2 ** 26)
thread = threading.Thread(target=main)
thread.start()