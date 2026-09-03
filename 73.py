n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
b = []
for i in range(n):
    b.append(int(input()))
min_shift = -1
for k in range(n):
    match = True
    for i in range(n):
        if b[i] != a[(i - k + n) % n]:
            match = False
            break
    if match:
        min_shift = k
        break
print(min_shift)