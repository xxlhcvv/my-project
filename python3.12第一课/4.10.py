for x in range(100,1000):
    flag = True
    for i in range(2, x):
        if x % i == 0:
            flag = False
            break
    if flag:
        print(x)
