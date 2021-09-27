for _ in range(int(input())):
    n = int(input())
    temp = len(bin(n).replace("0b", ""))
    num = (2**(temp-1))-1
    print(num)
