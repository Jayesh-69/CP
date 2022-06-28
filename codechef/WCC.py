for _ in range(int(input())):
    x = int(input())
    s = input()
    d = s.count('D')
    c = (s.count('C')*2) + d
    n = (s.count('N')*2) + d

    if c > n:
        print(60*x)
    elif c == n:
        print(55*x)
    else:
        print(40*x)