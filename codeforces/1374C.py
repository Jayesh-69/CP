for _ in range(int(input())):
    nn = int(input())
    n = input()
    bal = 0
    ans = 0
    for i in n:
        if i == '(':
            bal += 1
        else:
            bal -= 1
            if bal < 0:
                ans += 1
                bal = 0
    print(ans)
