a = 2
b = 2
c = 3
d = 3

if a == c or b == d:
    print('а) Ладья угрожает')
else:
    print('а) Ладья НЕ угрожает')

if abs(a - c) == abs(b - d):
    print('б) Слон угрожает')
else:
    print('б) Слон НЕ угрожает')

if abs(a - c) <= 1 and abs(b - d) <= 1:
    print('в) Король может попасть')
else:
    print('в) Король НЕ может попасть')

if (a == c or b == d) or (abs(a - c) == abs(b - d)):
    print('г) Ферзь угрожает')
else:
    print('г) Ферзь НЕ угрожает')

if a == c and d - b == 1:
    print('д) Пешка может пойти обычно')
else:
    print('д) Пешка НЕ может пойти обычно')

if abs(a - c) == 1 and d - b == 1:
    print('д) Пешка может побить')
else:
    print('д) Пешка НЕ может побить')