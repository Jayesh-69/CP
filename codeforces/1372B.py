for _ in range(int(input())):
    n = int(input())
    p = 0
    for i in range(2, 100000):
        if n % i == 0:
            p = i
            break
    if p == 0:
        p = n
    print(str((n//p))+" "+str((n-(n//p))))
