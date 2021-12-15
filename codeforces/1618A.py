for _ in range(int(input())):
    arr = list(map(int, input().split()))
    x = arr[0]
    y = arr[1]
    z = arr[-1]-x-y

    print(str(x)+" "+str(y)+" "+str(z))
