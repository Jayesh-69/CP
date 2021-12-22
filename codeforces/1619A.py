for _ in range(int(input())):
    s = input()
    n = len(s)
    if n % 2 == 0:
        if s[:n//2] == s[n//2:]:
            print("YES")
        else:
            print("NO")
    else:
        print("NO")
