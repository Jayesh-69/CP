for _ in range(int(input())):
    h, m = map(int, input().split())
    rM = 60-m
    h += 1
    rH = 24-h
    rM += (rH*60)
    print(rM)
