for _ in range(int(input())):
    n = int(input())
    a = input()

    if a.count('0') % 2 == 0 or a.count('0') == 1:
        print("BOB")
    else:
        print("ALICE")
