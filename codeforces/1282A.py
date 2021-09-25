for _ in range(int(input())):
    a, b, c, d = map(int, input().split())
    cS = c-d
    cE = c+d
    st = max(cS, min(a, b))
    ed = min(cE, max(a, b))
    print(abs(b-a)-max(0, ed-st))
