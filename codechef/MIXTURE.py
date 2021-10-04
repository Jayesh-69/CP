for _ in range(int(input())):
    A, B = map(int, input().split())
    if A > 0 and B > 0:
        print("Solution")
    elif B == 0:
        print("Solid")
    else:
        print("Liquid")
