for _ in range(int(input())):
    n = int(input())
    a = [int(i) for i in input().split()]
    mm = min(a)
    MM = max(a)

    lm = a.index(mm)
    rm = n-lm-1

    lM = a.index(MM)
    rM = n-lM-1

    if lm < rm and lM < rM:
        print(max(lm, lM)+1)
    elif lm > rm and lM > rM:
        print(max(rm, rM)+1)
    else:
        print(min(min(lm, rm)+min(lM, rM))+max(lM, rM)+2)
