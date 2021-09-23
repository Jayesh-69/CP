import math

for _ in range(int(input())):
    n = int(input())
    arr = [int(i) for i in input().split()]

    count = 0
    flag = False
    if sum(arr) == 0:
        if 0 in arr:
            arr[arr.index(0)] += 1
            count += 1
            flag = True
        else:
            arr[0] += 1
            count += 1
    if math.prod(arr) == 0:
        if flag:
            count += arr.count(0)-1
        else:
            count += arr.count(0)
    if abs(sum(arr)) == arr.count(0):
        count += 1
    print(count)
