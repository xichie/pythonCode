import math

while True:
    flag = True
    l = input().split(" ")
    if len(l) == 2:
        m, n = map(int, l)
        for num in range(m, n+1):
            a, b, c = map(int, [str(num)[0],str(num)[1],str(num)[2]])
            if (a**3 + b**3 + c**3) == num:
                print(num, end=' ')
                flag = False
        if flag:
            print('no', end=' ')
        print()