for _ in range(int(input())):
    x, y = map(int, input().split())
    s = input()
    l = s.count('L')
    r = s.count('R')
    u = s.count('U')
    d = s.count('D')

    if x >= 0 and y >= 0:
        if x <= r and y <= u:
            print("YES")
        else:
            print("NO")
    elif x >= 0 and y < 0:
        if x <= r and abs(y) <= d:
            print("YES")
        else:
            print("NO")
    elif x < 0 and y >= 0:
        if abs(x) <= l and y <= u:
            print("YES")
        else:
            print("NO")
    else:
        if abs(x) <= l and abs(y) <= d:
            print("YES")
        else:
            print("NO")
