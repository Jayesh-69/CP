for _ in range(int(input())):
    a, b, c = map(int, input().split())
    diff = abs(a-b)
    lim = diff*2
    if max(a, b, c) <= lim:
        # p = c+diff
        # s = c-diff
        mid = lim//2
        midPair = lim
        if c == mid:
            print(midPair)
        elif c > mid:
            print(c-mid)
        else:
            print(lim-(mid-c))
    else:
        print(-1)
