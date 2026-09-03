n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
max_count = 0
best_elem = a[0]
for i in range(len(a)):
    count = 0
    for j in range(len(a)):
        if a[i] == a[j]:
            count += 1
    if count > max_count:
        max_count = count
        best_elem = a[i]
print(best_elem)