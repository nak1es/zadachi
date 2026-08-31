x1, y1, w1, h1 = 0, 0, 2, 2
x2, y2, w2, h2 = 1, 1, 4, 3

r1 = x1 + w1
t1 = y1 + h1

r2 = x2 + w2
t2 = y2 + h2

if x1 >= x2 and y1 >= y2 and r1 <= r2 and t1 <= t2:
    print('а) Первый внутри второго')
else:
    print('а) Первый НЕ внутри второго')

if (x1 >= x2 and y1 >= y2 and r1 <= r2 and t1 <= t2) or (x2 >= x1 and y2 >= y1 and r2 <= r1 and t2 <= t1):
    print('б) Один лежит внутри другого')
else:
    print('б) Ни один не внутри другого')

if x1 < r2 and r1 > x2 and y1 < t2 and t1 > y2:
    print('в) Пересекаются')
else:
    print('в) НЕ пересекаются')