n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
res = []
for i in range(len(a)):
    already_in = False
    for j in range(len(res)):
        if res[j] == a[i]:
            already_in = True
            break
    if not already_in:
        res.append(a[i])
for i in range(len(res)):
    print(res[i], end=' ')