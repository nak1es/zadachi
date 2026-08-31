a, b, c = 2, 5, 10
x, y = 6, 4
kir = sorted([a, b, c])
otv = sorted([x, y])
if kir[0] <= otv[0] and kir[1] <= otv[1]:
    print('Пройдет')
else:
    print('Не пройдет')