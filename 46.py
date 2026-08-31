n = int(input('Число: '))
for i in range(10):
    a = n
    count = 0
    while a > 0:
        if a % 10 == i:
            count += 1
        a //= 10
    if count > 0:
        print(i, ':', count)