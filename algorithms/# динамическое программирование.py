# динамическое
# Вагнера-Фишера

s1, s2 = input(), input()

matrix = [[0 for j in range(len(s2) + 1)] for i in range(len(s1) + 1)]

for i in range(len(s1) + 1):
    for j in range(len(s2) + 1):
        if j == 0: # нумерация строк 
            matrix[i][j] = i
        elif i == 0: # нумерация столбцов
            matrix[i][j] = j
        elif s1[i - 1] == s2[j - 1]: # если символы в обеих строках совпали, сохраняем количество операций, указанное в матрице (по диагонали, на одну строку и на один столбец ранее)
            matrix[i][j] = matrix[i-1][j-1]
        else:
            # дальше ищем минимум среди возможных операций и прибавляем к минимуму единицу
            delete, insert, substitute = matrix[i - 1][j], matrix[i][j - 1], matrix[i - 1][j - 1]
            matrix[i][j] = min(delete, insert, substitute) + 1

print(matrix[len(s1)][len(s2)])