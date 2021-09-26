for _ in range(int(input())):
    n = int(input())
    a = [int(i) for i in input().split()]
    if sum(a) % n != 0:
        print(-1)
    else:
        temp = sum(a)//n
        count = 0
        for i in a:
            if i > temp:
                count += 1
        print(count)
