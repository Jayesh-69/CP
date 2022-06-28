for _ in range(int(input())):
    n = int(input())
    s = input()
    one = s.count("1")
    zero = s.count("0")
    if n == 1:
        print("YES")
    elif one == n or zero == n:
        print("yes")
    else:
        if n%2 != 0:
            print("YES")
        else:
            if one%2 == 0 and zero%2 == 0:
                print("YES")
            else:
                print("NO")