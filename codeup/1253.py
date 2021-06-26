a, b = input().split()
a = int(a)
b = int(b)

if a < b:
    for i in range(a, b+1):
        print(i, end=' ')
else:
    for i in range(b, a+1):
        print(i, end=' ')