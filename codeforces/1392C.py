for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(n-1):
        ans += max(a[i]-a[i+1], 0)
    print(ans)
