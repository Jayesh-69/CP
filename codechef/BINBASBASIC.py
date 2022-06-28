for _ in range(int(input())):
    n, k = map(int, input().split())
    s = input()
    if k == 0 and s == s[::-1]:
        print("YES")
    elif k == 0:
        print("NO")
    elif n == 1:
        print("YES")
    else:
        if n % 2 == 0:
            sl = s[:n//2]
            sr = s[n//2:]
        else:
            sl = s[:n//2]
            sr = s[n//2+1:]
        sr = sr[::-1]
        temp = str(int(sr)+int(sl))
        if temp.count("1") == k:
            print("YES")
        else:
            print("NO")
