# bfs

def check(x, y):
    return  x >= 0 and x < n and y >= 0 and y < n

def bfs():
    while queue: # пока очередь не пуста
        x, y = queue.pop(0)
        for i in range(8):
            xn = x + DX[i]
            yn = y + DY[i]
            if check(xn, yn) and not used[xn][yn]:
                used[xn][yn] = [x, y]
                queue.append([xn, yn])
                if finish == [xn, yn]:
                    return 
                
read_raw = [
    '20',
    '1 1',
#     '5 5'
#     '20 20',
    '3 2',
]

n = int(read_raw[0])
start = list(map(int, read_raw[1].split()))
finish = list(map(int, read_raw[2].split()))

start[0] -= 1
start[1] -= 1
finish[0] -= 1
finish[1] -= 1

used = [[False for _ in range(n)] for _ in range(n)]
used[start[0]][start[1]] = [start[0], start[1]]
queue = [start]
bfs()

way = [finish]
while finish != start:
    finish = used[finish[0]][finish[1]]
    way.append(finish)

way.reverse()
print(len(way))
for i in way:
    print(i[0] + 1, i[1] + 1)