for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort(reverse=True)
    intialG = n

    for i in arr:
        if i <= intialG:
            break
        intialG -= 1
    print(intialG+1)
