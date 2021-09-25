for _ in range(int(input())):
    n, k = map(int, input().split())
    childWithOneMore = k//2
    if n % k == 0:
        print(n)
    else:
        count = ((n//k)*k) + min(childWithOneMore, n % k)
        print(count)
