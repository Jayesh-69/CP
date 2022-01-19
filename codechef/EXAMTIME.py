for _ in range(int(input())):
    d = list(map(int, input().split()))
    s = list(map(int, input().split()))
    if sum(d) > sum(s):
        print("DRAGON")
    elif sum(d) < sum(s):
        print("SLOTH")
    else:
        flag = True
        for i in range(3):
            if d[i] > s[i]:
                print("DRAGON")
                flag = False
                break
            if d[i] < s[i]:
                flag = False
                print("SLOTH")
                break
        if flag:
            print("TIE")
