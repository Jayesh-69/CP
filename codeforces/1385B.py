for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    newA = []
    for i in a:
        if i not in newA:
            newA.append(i)
    for i in newA:
        print(i, end=" ")
    print()
