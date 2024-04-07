# снова dfs, решила делать рекурсивно, раз уж был озвучен трюк с параллелизмом
from sys import setrecursionlimit
import threading

def main():
    def dfs(v, color, cur):
        color[v] = cur
        for u in adjacency_list[v]:
            if color[u] == 0:
                dfs(u, color, cur)

    read_raw = [
        '4 2',
        '1 3',
        '2 4',
    ]

    n, m = map(int, read_raw[0].split())

    color = [0 for _ in range(n)]
    adjacency_list = [set() for _ in range(n)]

    for row in read_raw[1:]:
        v1, v2 = map(int, row.split())
        if v1 != v2:
            adjacency_list[v1 - 1].add(v2 - 1)
            adjacency_list[v2 - 1].add(v1 - 1)

    cnt = 0
    for vertes in range(n):
        if color[vertes] == 0:
            cnt += 1
            dfs(vertes, color, cnt)
        
    print(cnt)
    print(*color)
    
# пусть будет как в чате
setrecursionlimit(10 ** 9)
threading.stack_size(2 ** 26)
thread = threading.Thread(target=main)
thread.start()