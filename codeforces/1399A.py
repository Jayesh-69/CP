for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    flag = True
    for i in range(n-1):
        if abs(a[i] - a[i+1]) <= 1:
            continue
        flag = False
        break
    print("YES" if flag else "NO")
