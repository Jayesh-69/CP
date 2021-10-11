for _ in range(int(input())):
    a, b, n, m = map(int, input().split())
    if n+m <= a+b and m <= min(a, b):
        print("YES")
    else:
        print("NO")
