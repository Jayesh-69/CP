for _ in range(int(input())):
    n, m = map(int, input().split())
    print(((n*m)//2) if (n*m) % 2 == 0 else (((n*m)//2)+1))
