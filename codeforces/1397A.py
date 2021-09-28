for _ in range(int(input())):
    n = int(input())
    s = ""
    for i in range(n):
        s += input()
    arr = list(set(s))
    count = 0
    flag = True
    for i in arr:
        count = s.count(i)
        if count % n == 0:
            continue
        else:
            flag = False
    print("YES" if flag else "NO")
