for _ in range(int(input())):
    n = int(input())
    ath = []
    for i in range(n):
        ath.append([int(i) for i in input().split()])

    w = 0

    for i in range(1, n):
        count = 0
        for j in range(5):
            if ath[i][j] > ath[w][j]:
                count += 1
        if count < 3:
            w = i
    for i in range(n):
        if i == w:
            continue
        count = 0
        for j in range(5):
            if ath[i][j] > ath[w][j]:
                count += 1
        if count < 3:
            w = -2
            break
    print(w+1)
