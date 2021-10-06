for _ in range(int(input())):
    n = input()
    cz = n.count('0')
    co = n.count('1')

    if cz == 0 or co == 0:
        print("NET")
    else:
        minm = min(cz, co)
        if minm % 2 == 0:
            print("NET")
        else:
            print("DA")
