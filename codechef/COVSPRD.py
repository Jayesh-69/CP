for _ in range(int(input())):
    n, d = map(int, input().split())
    if d <= 10:
        temp = 2**d
        print(min(n, temp))
    else:
        temp = 1024
        d -= 10
        temp *= (3**d)
        print(min(n, temp))
