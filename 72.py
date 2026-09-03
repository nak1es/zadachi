n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
b = []
for i in range(n):
    b.append(int(input()))
possible = False
for shift in range(n):
    match = True
    for i in range(n):
        if a[i] != b[(i + shift) % n]:
            match = False
            break
    if match:
        possible = True
        break
if possible:
    print('Да')
else:
    print('Нет')