n = int(int(input()))
x = list(map(int, input().split()))
c = list(map(int, input().split()))

c.sort()
flag = True
for i in range(n):
    if c[i] < x[i]:
        flag = False
        break
if flag:
    print("YES")
else:
    print("NO")
