n = int(input())
a = []
for i in range(n):
    b = int(input())
    a.append(b)
max= 1
current = 1
for i in range(1, len(a)):
    if a[i] < a[i-1]:
        current += 1
        if current > max:
            max = current
    else:
        current = 1
print(max)