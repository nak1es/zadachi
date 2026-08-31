n = int(input('Сколько чисел будем вводить? '))
for i in range(n):
    n = int(input())
    if n % 2 == 0:
        print('Четное')
    else:
        print('Нечетное')