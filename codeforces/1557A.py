for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    sumAvg = max(arr) + (sum(arr)-max(arr))/(n-1)
    print(sumAvg)
