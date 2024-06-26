# указатели (кривые)

n, m = map(int, input().split())
s = input()
cards = input()

s_letters_idx = [ord(char) - ord('a') for char in s] # список индексов букв в строке (за 0 берем латинскую a)
 
cards_letters_num = [0] * 26
for card in cards: # количество карточек (соответственно алфавиту)
    cards_letters_num[ord(card) - ord('a')] += 1

res, left, right = 0, 0, 0 # ответ и два указателя

# дальше двигаем правый указатель, пытаясь получить подстроку, которую можно собрать из карточек
# когда карточки для составления данной подстроки закончатся, будем передвигать левый указатель
 
while left < n: # будем перебирать пока левый указатель не дойдет до конца исходной строки
    res += right - left # прибавляем разницу между указателями (количество подстрок, которые можно собрать из карточек)
    right += 1 # двигаем правый указатель
    if right > n:
        break
    # выбираем из букв в строке символ с индксом, равным позиции правого указателя и вычитаем карточку с буквой из списка карточек
    cards_letters_num[s_letters_idx[right - 1]] -= 1
    if cards_letters_num[s_letters_idx[right - 1]] < 0: # если карточек с буквой больше не осталось, двигаем левый указатель
        while True:
            idx = s_letters_idx[left] # выбираем из букв в строке символ с индексом, равным позиции левого указателя
            cards_letters_num[idx] += 1 # восстанавливаем карточку, которую ранее вычли
            left += 1 # двигаем левый указатель
            if cards_letters_num[idx] == 0: # если после восстановления 0 карточек, продолжаем двигать правый указатель
                break

print(res)