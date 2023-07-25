#Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

n = int(input('Введите число: '))
stop = 0
k = 2
for i in range(n):
    if stop != 1:
        k = k ** i
        if k <= n:
            print(k, end=' ')
            k = 2
        else:
            stop = 1
    else:
        i = n