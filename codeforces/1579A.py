for _ in range(int(input())):
    n = input()
    a = n.count('A')
    b = n.count('B')
    c = n.count('C')

    if b == a+c:
        print("YES")
    else:
        print("NO")
