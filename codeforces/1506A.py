for _ in range(int(input())):
    k = int(input())
    arr = []
    i = 1
    while k != 0:
        if i % 3 == 0 or i % 10 == 3:
            i += 1
            continue
        arr.append(i)
        i += 1
        k -= 1
    print(arr[-1])
