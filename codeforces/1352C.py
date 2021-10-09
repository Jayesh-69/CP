import math
for _ in range(int(input())):
    N, K = map(int, input().split())
    print(K + math.floor((K - 1) / (N - 1)))
