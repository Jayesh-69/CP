for _ in range(int(input())):
    a = [int(i) for i in input().split()]
    sun = a.count(1)
    rain = a.count(0)

    if sun > rain:
        print("YES")
    else:
        print("NO")
