n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
max_sum = a[0]
for i in range(len(a)):
    current_sum = 0
    for j in range(i, len(a)):
        current_sum += a[j]
        if current_sum > max_sum:
            max_sum = current_sum
print(max_sum)