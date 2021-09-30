for _ in range(int(input())):
    A, B, n = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    totalDamage = 0
    flag = True
    for i in range(n):
        totalDamage += (b[i]+A-1)//A*a[i]
    for i in range(n):
        if B-(totalDamage-a[i]) > 0:
            print("YES")
            flag = False
            break
    if flag:
        print("NO")
