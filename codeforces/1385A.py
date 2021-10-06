for _ in range(int(input())):
    a = list(map(int, input().split()))
    a.sort()
    if a[1] != a[2]:
        print("NO")
    else:
        print("YES")
        print(str(a[0])+" "+str(a[0])+" "+str(a[2]))
