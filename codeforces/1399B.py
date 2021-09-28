for _ in range(int(input())):
    n = int(input())
    c = list(map(int, input().split()))
    o = list(map(int, input().split()))

    count = 0
    minC = min(c)
    minO = min(o)

    for i in range(n):
        if c[i] == minC and o[i] == minO:
            continue
        elif c[i] == minC and o[i] != minO:
            count += o[i]-minO
        elif c[i] != minC and o[i] == minO:
            count += c[i]-minC
        else:
            count += max((o[i]-minO), (c[i]-minC))
    print(count)
