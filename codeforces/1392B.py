import numpy as np

for _ in range(int(input())):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    if k % 2 == 0:
        k = 2
    else:
        k = 1
    for i in range(k):
        aa = np.array(a)
        temp = max(a)
        aa = temp-aa
        a = aa.tolist()
    for i in range(n):
        if i == n-1:
            print(a[i])
        else:
            print(a[i], end=" ")
