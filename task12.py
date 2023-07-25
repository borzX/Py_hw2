

s = int(input('Введите сумму чисел: '))
p = int(input('Введите произведение чисел: '))
a = 0
if s > 2000 or p > 1000000:
    print ('Вы ввели не корректные данные!')
else:
    for x in range(s):
        for y in range(s):
            if x + y == s and x * y == p:
                a += 1
                print(x, y)
if a == 0:
    print('Вы ввели не корректные данные!')