def prime(a):
    for i in range(1, a):
        for j in range(2, i):
            if not (i % j == 0):
                num.append(i)
    print(num)


num = []
prime(20)
