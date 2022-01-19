for _ in range(int(input())):
    n = int(input())
    r = []
    g = []
    b = []
    for _ in range(3):
        x, y, z = map(int, input().split())
        r.append(x)
        g.append(y)
        b.append(z)
    print(max(g[0]+b[0]+b[1], r[1]+r[2]+g[2]))
