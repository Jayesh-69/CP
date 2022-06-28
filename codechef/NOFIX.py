for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    k = 0
    for i in range(n):
        temp = 1+i+k
        if temp == a[i]:
            k += 1
    print(k)