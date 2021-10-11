for _ in range(int(input())):
    a, b, c, n = map(int, input().split())
    if n == 0:
        print("YES")
    else:
        N = a//2+b//2+c//2
        if n == N:
            print("YES")
        else:
            print("NO")
