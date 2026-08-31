for i in range(10, 100):
    fir = i // 10
    sec = i % 10
    if (fir + sec) ** 2 == i:
        print(i)