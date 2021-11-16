for _ in range(int(input())):
    n, m = map(int, input().split())
    count = 0
    for i in range(n):
        temp = input()
        if temp[-1] == 'R':
            count += 1
    count += temp.count('D')
    print(count)
