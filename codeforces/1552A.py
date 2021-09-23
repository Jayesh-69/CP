for _ in range(int(input())):
    n = int(input())
    s = input()
    temp = ''.join(sorted(s))
    count = 0
    for i in range(n):
        if s[i] != temp[i]:
            count += 1
    print(count)
