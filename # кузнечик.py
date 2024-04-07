# кузнечик

n, k = map(int, input().split())
a = list(map(int, input().split()))
b = [0] * (len(a) - 1)

for i in range(1, len(a)):
    b[i-1] = a[i] * (a[i] > 0 or a[i] == max(a[i: i+k]))

print(sum(b))
print(len(filter(lambda x: x != 0, b)))
print(*[n for n, v in enumerate(b, 1) if v != 0])





n, m = map(int, input().split())
a = list(map(int, input().split()))

a = [0] + a + [0]
way = [1]

count = 1

for i in range(2, n):
    indices = [i - j for j in range(1, m + 1)]
    tmp = None
    index_max = 0
    for index in indices:
        if index >= 0 and (tmp is None or a[index] > tmp):
            index_max = index
            tmp = a[index]
            
    a[i] += tmp

    if index_max + 1 != way[-1]:
        way.append(index_max + 1)
        count += 1
    
way.append(n)

print(a[-1])
print(count)
print(*way)