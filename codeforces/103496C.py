n, h, k = map(int, input().split())
maxD = 0
for i in range(n):
    x, y = map(int, input().split())
    d = (((x-h)**2)+((y-k)**2))**(1/2)
    maxD = max(d, maxD)
print(2*maxD)
