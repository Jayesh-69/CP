for _ in range(int(input())):
    a, b, n = map(int, input().split())
    if max(a, b) > n:
        print(0)
    else:
        count = 0
        while max(a, b) <= n:
            temp = a+b
            if a < b:
                a = temp
            else:
                b = temp
            count += 1
    print(count)
