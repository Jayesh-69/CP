for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    if sum(a) == n:
        print(0)
    elif sum(a) < n:
        print(1)
    else:
        print(sum(a)-n)
