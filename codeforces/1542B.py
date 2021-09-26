for _ in range(int(input())):
    n, a, b = map(int, input().split())
    if a == 1:
        if (n-1) % b == 0:
            print("Yes")
        else:
            print("No")
    else:
        t = 1
        flag = 0
        while t <= n:
            if t % b == n % b:
                flag = 1
                break
            t = t*a
        if flag == 1:
            print("Yes")
        else:
            print("No")
