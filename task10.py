# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были 
# повернуты вверх одной и той же стороной. Выведите минимальное количество монет, которые нужно перевернуть

n = int(input('Введите количество монет: '))
orl = 0
rsh = 0
for i in range(n):
    x = int(input('Орел(1) или Решка(0)? '))
    if x == 1:
        orl += 1
    elif x == 0:
        rsh += 1
    else:
        orl = 0
        rsh = 0
        #print(f'Вы ввели не верное значение')
        break
if orl == rsh ==0:
    print(f'Вы ввели не верное значение')
elif orl < rsh:
    print(f'Переверните {orl} монет с орла на решку, их меньше всего')
elif orl == rsh > 0:
    print(f'Количество орлов и решек одинаково, по {orl} штук')
elif orl > rsh:
    print((f'Переверните {rsh} монет с решки на орла, их меньше всего'))    
