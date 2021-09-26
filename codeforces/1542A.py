for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    cE = 0
    cO = 0
    for i in a:
        if i % 2 == 0:
            cE += 1
        else:
            cO += 1
    if cE == cO:
        print("YES")
    else:
        print("NO")
