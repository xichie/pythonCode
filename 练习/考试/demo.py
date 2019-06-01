import math

while True:
    l = input().split(" ")
    num = 0
    if len(l) == 2:
        m, n = map(int, l)
        for i in range(n):
            num += m
            m = math.sqrt(m)
        print('%.2f'%num)