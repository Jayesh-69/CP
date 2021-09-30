for _ in range(int(input())):
    s = input()
    newS = ""
    for i in range(len(s)):
        if i % 2 == 0:
            if s[i] == 'a':
                newS += 'b'
            else:
                newS += 'a'
        else:
            if s[i] == 'z':
                newS += 'y'
            else:
                newS += 'z'
    print(newS)
