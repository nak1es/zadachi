n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
max_len = 0
for i in range(n):
    for j in range(i, n):
        duplicate = False
        for k in range(i, j):
            if a[k] == a[j]:
                duplicate = True
                break
        if duplicate:
            break
        current_len = j - i + 1
        if current_len > max_len:
            max_len = current_len
print(max_len)