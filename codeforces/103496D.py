n = int(input())
nums = list(map(int, input().split()))
nums.sort()

nThanx = 0
for i in nums:
    if i <= nThanx:
        nThanx += 1
print(nThanx)
