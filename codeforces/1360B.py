for _ in range(int(input())):
    n = int(input())
    arr = [int(i) for i in input().split()]
    arr.sort()
    count = 99999999999999999

    for i in range(n-1):
        diff = arr[i+1]-arr[i]
        if diff < count:
            count = diff
    print(count)
