n = int(input())
a = []
for i in range(n):
    b = int(input())
    a.append(b)
flag = False
for i in range(1, len(a) - 1):
    if a[i] > a[i-1] and a[i] > a[i+1]:
        print(a[i])
        flag = True
        break
if flag == False:
    print('no')