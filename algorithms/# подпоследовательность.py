# динамическое
# перебор n элементов (и на каждой итерации всех предшествующих n-тому) с сохранением индекса предыдущего элемента и длины подпоследовательности, оканчивающейся на n-тый элемент

n = int(input())
array = list(map(int, input().split()))

lens = [1] * n # список с длинами подпоследовательностей, оканчивающихся n-тым элементом исходной последовательности
prev_idx = [None] * n # список с индексами предшествующих элементов для n-того элемента исходной последовательности

for i in range(1, n): # перебор всех чисел с первого индекса, т.к. по нулевому уже имеются и длина, и индекс предшествующего элемента
    for j in range(i): # перебор всех чисел, предшествующих i-тому
        # i-тое число должно быть больше предыдущего (по условию), и тогда
        # для переприсвоения новой (большей) длины текущая длина подпоследовательности,
        # которая оканчивается на i-тое число должна быть меньше, чем длина подпоследовательности,
        # оканчивающейся на j-тое, плюс единица (единица - само j-тое число)
        if array[i] > array[j] and lens[i] < lens[j] + 1:
            prev_idx[i] = j 
            lens[i] = lens[j] + 1

res = []

# допустим, что в массиве не может быть двух возрастающих подпоследовательностей с одинаковой (максимальной) длиной
max_subseq_len_idx = lens.index(max(lens)) 

# раскручиваем все в обратную сторону (с конца по списку длин подпоследовательностей):
# исходя из того, что имеем индекс максимальной длины последовательности,
# имеем и индекс (из исходной подпоследовательности) конечного элемента макс. возр. подп-ти,
# (каждый следующий элемент добавляем в начало списка)
# в качестве индекса конечного элемента переприсваиваем значение индекса предыдущего элемента
while max_subseq_len_idx != None:
    res.insert(0, array[max_subseq_len_idx])
    max_subseq_len_idx = prev_idx[max_subseq_len_idx]

print(f"{len(res)}\n{' '.join(map(str, res))}")