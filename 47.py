n = int(input('n: '))
for i in range(2, n + 1):
    flag = True
    for delit in range(2, i):
        if i % delit == 0:
            flag = False
            break
    if flag == True:
        print(i, end=' ')
print()