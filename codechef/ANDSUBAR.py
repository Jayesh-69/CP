for _ in range(int(input())):
    n = int(input())
    if n < 3:
        print(1)
    else:
        arr = []
        i = 1
        while i <= n:
            arr.append(i)
            i *= 2
        fd = n-arr[-1]
        sd = arr[-1]-arr[-2]-1
        print(max(fd, sd)+1)
