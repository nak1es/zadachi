n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
found = False
for i in range(len(a)):
    current_sum = a[i]
    for j in range(i + 1, len(a)):
        current_sum += a[j]
        if current_sum == 0:
            found = True
            break
    if found:
        break
if found:
    print('Да')
else:
    print('Нет')