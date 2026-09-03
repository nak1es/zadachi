n = int(input())
a = []
for i in range(n):
    b = int(input())
    a.append(b)
max = 0
for i in range(1, len(a)):
    if a[i] > a[max]:
        max = i
print(max)