n = int(input('Число: '))
a = n
reverse = 0
while n > 0:
    a = n % 10
    reverse = reverse * 10 + a
    n //= 10
if a == reverse:
    print('Да')
else:
    print('Нет')