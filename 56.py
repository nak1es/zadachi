n = int(input())
a = []
for i in range(n):
    b = int(input())
    a.append(b)
count = 0
for i in range(len(a)):
    if a[i] % 2 == 0:
        count += 1
print(count)