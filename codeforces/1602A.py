for _ in range(int(input())):
    s = input()
    a = ''.join(sorted(s))[0]
    b = ''
    flag = True
    for i in s:
        if i == a and flag:
            flag = False
            continue
        b += i
    print(a+" "+b)
