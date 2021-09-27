for _ in range(int(input())):
    n, k = map(int, input().split())
    maxStay = 0
    for i in range(n):
        s, e = map(int, input().split())
        if s <= k:
            temp = (e-k)+1
        if temp > maxStay:
            maxStay = temp

    print(maxStay)
