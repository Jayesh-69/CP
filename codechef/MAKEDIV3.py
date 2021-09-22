for _ in range(int(input())):
    n = int(input())
    num = int("1"+"0"*(n-1))+2
    while True:
        if num % 9 != 0 and num % 2 != 0:
            print(num)
            break
        else:
            num += 3
