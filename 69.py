n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
max_sum = a[0]
best_start = 0
best_end = 0
for i in range(len(a)):
    current_sum = 0
    for j in range(i, len(a)):
        current_sum += a[j]
        if current_sum > max_sum:
            max_sum = current_sum
            best_start = i
            best_end = j
print(best_start, best_end)