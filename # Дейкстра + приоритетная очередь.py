# Дейкстра + приоритетная очередь
import heapq

INF = float('inf')

read_raw = [
    '4 5',
    '1 2 1',
    '1 3 5',
    '2 4 8',
    '3 4 1',
    '2 3 3',
]

n = int(read_raw[0].split()[0])

queue = []
heapq.heappush(queue, (0, 0))

edges = [[] for _ in range(n)]

for raw in read_raw[1:]:
    u, v, w = map(int, raw.split())
    edges[u - 1].append((w, v - 1))
    edges[v - 1].append((w, u - 1))

distance = [INF for _ in range(n)]
distance[0] = 0

used = [False for _ in range(n)]

while queue:
    _, u = heapq.heappop(queue)
    if used[u]:
        continue
        
    used[u] = True

    for w, to in edges[u]:
        if distance[u] + w < distance[to]:
            distance[to] = distance[u] + w
            heapq.heappush(queue, (distance[to], to))

print(*distance)