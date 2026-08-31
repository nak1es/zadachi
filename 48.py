n = int(input('Число: '))
max = 0
count = 1
prev = -1
while n > 0:
    a = n % 10
    if a == prev:
        count += 1
    else:
        if count > max:
            max = count
        count = 1
        prev = a
    n //= 10
if count > max:
    max = count
print(max)