for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    count = 0
    for i in range(1, n+1):
        if a[i-1] <= i+count:
            continue
        count += (a[i-1]-(i+count))
    print(count)
