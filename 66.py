n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
max_len = 0
for i in range(len(a)):
    current_sum = 0
    for j in range(i, len(a)):
        current_sum += a[j]
        if current_sum == 0:
            current_len = j - i + 1
            if current_len > max_len:
                max_len = current_len
print(max_len)