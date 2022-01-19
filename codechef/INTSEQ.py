import math
for _ in range(int(input())):
    k = int(input())
    count = 0
    while True:
        if k % 2 == 0:
            count += 1
            k = k//2
            continue
        break
    print(count)
