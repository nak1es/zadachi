n = int(input())
a = []
for i in range(n):
    b = int(input())
    a.append(b)
flag = True
for i in range(len(a) // 2):
    if a[i] != a[len(a) - 1 - i]:
        flag = False
        break
if flag == True:
    print('Да')
else:
    print('Нет')