for _ in range(int(input())):
    n = int(input())
    arr = list(input().split())

    s = arr[0]

    for i in range(1, len(arr)):
        if arr[i-1][1] == arr[i][0]:
            s += arr[i][1]
        else:
            s += arr[i]

    if len(s) == n:
        print(s)
    else:
        print(s+"a")
