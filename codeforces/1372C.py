for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    if sorted(a) == a:
        print(0)
    else:
        aa = sorted(a)
        count = 0
        for i in range(n):
            if aa[i] == a[i]:
                count += 1
        if count == 0:
            print(1)
        else:
            print(2)
