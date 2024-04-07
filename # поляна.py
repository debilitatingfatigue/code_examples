# тернарный поиск

v_p, v_f = map(int, input().split())
a = float(input())
left_border = 0
right_border = 1
restr = 10**-5 # абсолютная погрешность

while right_border - left_border > restr: # пока разность границ не достигла погрешности
    middle_1 = (2 * left_border + right_border) / 3
    middle_2 = (2 * right_border + left_border) / 3
    # если время из middle_1 меньше, чем из middle_2, двигаем правую границу и присваиваем ей значение middle_2, в противном случае присваиваем левой границе значение middle_1
    if ((middle_1 ** 2 + (1 - a) ** 2) ** 0.5) / v_p + (((1 - middle_1) ** 2 + a ** 2)**0.5) / v_f < ((middle_2 ** 2 + (1 - a) ** 2) ** 0.5) / v_p + (((1 - middle_2) ** 2 + a ** 2) ** 0.5) / v_f:
        right_border = middle_2
    else:
        left_border = middle_1

print(left_border)