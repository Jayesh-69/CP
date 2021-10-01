for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    first = b[0]
    count = 0
    for i in range(n):
        if first > a[i]:
            break
        count += 1
    print(count)
