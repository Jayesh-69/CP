import math
for _ in range(int(input())):
    a, b = map(int, input().split())
    gcd = abs(a-b)
    if gcd == 0:
        print("0 0")
    else:
        print(str(gcd)+" "+str(min(a % gcd, (gcd-a) % gcd)))
