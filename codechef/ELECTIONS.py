for _ in range(int(input())):
    X = list(map(int, input().split()))
    if max(X) > 50:
        temp = X.index(max(X))
        if temp == 0:
            print("A")
        elif temp == 1:
            print("B")
        else:
            print("C")
    else:
        print("NOTA")
