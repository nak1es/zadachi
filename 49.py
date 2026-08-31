n = int(input('Число: '))
flag = True
prev = n % 10
n //= 10
while n > 0:
    a = n % 10
    if a >= prev:
        flag = False
        break
    prev = a
    n //= 10
if flag == True:
    print('Да')
else:
    print('Нет')