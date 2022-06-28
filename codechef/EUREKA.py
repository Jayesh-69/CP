import math
for _ in range(int(input())):
    n = int(input())
    temp = (0.143*n)**n
    if temp-int(temp) < 0.5:
        print(int(temp))
    else:
        print(int(temp)+1)
