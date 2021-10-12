[(lambda n: (lambda arr: [print(f'{arr[i]} {arr[i+n]}', end=' \n'[i == n-1]) for i in range(n)])(
    sorted(list(map(int, input().split())))))(int(input())) for _ in range(int(input()))]
