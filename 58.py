n = int(input())
a = []
for i in range(n):
    b = int(input())
    a.append(b)
last = -1
for i in range(1, len(a) - 1):
    if a[i] < a[i-1] and a[i] < a[i+1]:
        last = i
if last == -1:
    print('no')
else:
    print(last)