import math
for _ in range(int(input())):
    k = int(input())
    temp = int(math.sqrt(k))
    if temp**2 != k:
        temp += 1
    prevSum = ((temp-1)**2)
    diff = (k-prevSum)-1
    a, b = 1, temp
    if diff <= temp-1:
        print(str(a+diff)+" "+str(b))
    else:
        diff = (diff-(temp-1))
        print(str(temp)+" "+str(b-diff))
