# Требуется вывести все целые степени двойки (т.е. числа вида 2k),
# не превосходящие числа N.
# Пример:
# 10 -> 1 2 4 8

number = 0
n = int(input('введите число : '))
for k in range(0,100):
    number = 2 ** k
    if number > n:
        break
    print(number)
    

