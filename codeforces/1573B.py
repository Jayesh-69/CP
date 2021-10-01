for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    first = b[0]
    temp = 0
    for i in range(n):
        if first > a[i]:
            break
        temp += 1
    print(temp)
