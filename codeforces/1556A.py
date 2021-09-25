for _ in range(int(input())):
    c, d = map(int, input().split())
    if c == d and c == 0:
        print(0)
    elif c == d:
        print(1)
    elif abs(c-d) % 2 == 0:
        print(2)
    else:
        print(-1)
