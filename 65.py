n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
unique = []
duplicates = []
for i in range(len(a)):
    count = 0
    for j in range(len(a)):
        if a[i] == a[j]:
            count += 1
    if count == 1:
        unique.append(a[i])
    else:
        already_in = False
        for k in range(len(duplicates)):
            if duplicates[k] == a[i]:
                already_in = True
                break
        if not already_in:
            duplicates.append(a[i])
for i in range(len(unique)):
    print(unique[i], end=' ')
for i in range(len(duplicates)):
    print(duplicates[i], end=' ')