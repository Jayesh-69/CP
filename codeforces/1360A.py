for _ in range(int(input())):
    a, b = map(int, input().split())
    sqr1 = max(2*a, b)**2
    sqr2 = max(a, 2*b)**2
    print(min(sqr1, sqr2))
