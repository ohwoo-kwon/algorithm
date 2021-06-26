a, b = input().split()
a = int(a)
b = int(b)

for i in range(a, b+1):
    if i % 2:
        print(i, end=' ')