# dfs
from collections import defaultdict

def dfs(v, d=1): # просто стандартный обход дерева в глубину, аргументы функции: название вершины и длина цепочки (по умолчанию 1, .к. имеем как минимум один узел в цепочке)
    deep_dict[v] = d # вершине, которую посетили, присваиваем значение глубины, на которой она располагается в графе
    max_deep = d
    for u in adjacency_list[v]: # перебор всех вершин на один уровень ниже
        if deep_dict[u] == 0: # если еще не посещали вершину
            tmp_deep = dfs(u, d + 1) # рекурсивно считаем глубину цепочки с вершиной, которую посещаем впервые
            if tmp_deep > max_deep:
                max_deep = tmp_deep
    return max_deep

reposts = int(input())

adjacency_list = defaultdict(set) # список смежности
deep_dict = defaultdict(int) # словарь с уровнями вершин

for i in range(reposts):
    repost = input()
    v1, reposted, v2 = repost.lower().split()
    adjacency_list[v1].add(v2)
    adjacency_list[v2].add(v1)
    deep_dict[v1] = 0 # изначально вершинам присваиваем нулевой уровень, чтобы потом переприсвоить по мере обхода графа
    deep_dict[v2] = 0

print(dfs('polycarp')) # корневым узлом всегда будет Поликарп