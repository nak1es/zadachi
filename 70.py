n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
possible = False
for split_index in range(1, len(a)):
    left_sum = 0
    for i in range(0, split_index):
        left_sum += a[i]
    right_sum = 0
    for i in range(split_index, len(a)):
        right_sum += a[i]

    if left_sum == right_sum:
        possible = True
        break
if possible:
    print('Да')
else:
    print('Нет')