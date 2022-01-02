names = ["Alice", "Bob", "Cindy", "Dani"]
arr = input().split()
for i in names:
    if i not in arr:
        print(i)
        break
