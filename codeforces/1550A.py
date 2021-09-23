def maxSum(x):
    return x ** 2


t = int(input())
for i in range(t):
    x = int(input())
    res = 1
    while maxSum(res) < x:
        res += 1
    print(res)
