n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
found = False
for i in range(len(a)):
    count = 0
    for j in range(len(a)):
        if a[i] == a[j]:
            count += 1
    if count == 1:
        print(a[i], end=' ')
        found = True
if not found:
    print('no')