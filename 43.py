n = int(input('Число: '))
max = -1
max1 = -1
while n > 0:
    a = n % 10
    if a > max1:
        max1 = max
        max = a
    elif a > max1 and a != max:
        max1 = a
    n //= 10

if max1 == -1:
    print('нет')
else:
    print(max1)