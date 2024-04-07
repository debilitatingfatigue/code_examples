# динамическое

n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for i in range(n)]

for i in range(n): # пересчитываем матрицу, считая (максимально!!), сколько монет суммарно будет иметь черепаха на той или иной клетке
    for j in range(m):
        if i == 0 and j == 0:
            None
        elif i == 0 and j != 0: # заполнение нулевой строки матрицы (в каждой j-той клетке суммируются монеты за предыдущие клетки в строке и значение j-той)
            matrix[i][j] += matrix[i][j - 1] 
        elif j == 0 and i != 0: # заполнение нулевой колонки матрицы (в каждой i-той клетке суммируются монеты за предыдущие клетки в колонке и значение i-той)
            matrix[i][j] += matrix[i - 1][j]
        else: # к значениям остальных клеток (перебор идет построчно) прибавляем максимум из чисел сверху или слева от данной клетки
            matrix[i][j] += max(matrix[i][j - 1], matrix[i - 1][j])

max_coins = matrix[-1][-1]

path = []
i, j = n - 1, m - 1
while i > 0 or j > 0:
    if i == 0 or (j != 0 and matrix[i][j - 1] > matrix[i - 1][j]):
        path.append('R')
        j -= 1
    else:
        path.append('D')
        i -= 1

print(f"{max_coins}\n{' '.join(path[::-1])}")