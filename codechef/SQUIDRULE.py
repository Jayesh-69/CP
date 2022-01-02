for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    s = sum(arr)-min(arr)
    print(s)
