n = int(input('Число: '))
max = 0
while n > 0:
    a = n % 10
    if a > max:
        max = a
    n //= 10
print(max)