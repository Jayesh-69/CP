A = [[1, 2], [4, 5]]
arr = []
n = len(A)
i = 0
j = 0
for k in range(n):
    temp = []
    temp.append(A[i][j])
    ii = i
    jj = j
    while j-1 >= 0 and i < n:
        temp.append(A[i+1][j-1])
        i += 1
        j -= 1
    arr.append(temp)
    j = jj+1
    i = ii
i = 1
j = n-1
for k in range(n-1):
    temp = []
    temp.append(A[i][j])
    ii = i
    jj = j
    while i < n-1:
        temp.append(A[i+1][j-1])
        i += 1
        j -= 1
    arr.append(temp)
    j = jj
    i = ii+1
print(arr)
