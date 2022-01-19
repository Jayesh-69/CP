for _ in range(int(input())):
    n, x = map(int, input().split())
    X = list(map(int, input().split()))
    if sum(X) < x:
        print(-1)
    elif sum(X) == x:
        print(n)
    else:
        X.sort(reverse=True)
        count = 0
        temp = 0
        for i in X:
            temp += i
            if temp < x:
                count += 1
                continue
            count += 1
            break
        print(count)
