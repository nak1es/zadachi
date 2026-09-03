n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
max_count = 0
for i in range(n):
    count = 0
    for j in range(n):
        if a[i] == a[j]:
            count += 1
    if count > max_count:
        max_count = count
if max_count <= (n + 1) // 2:
    print('Да')
else:
    print('Нет')