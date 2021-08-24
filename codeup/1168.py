a, b = input().split()
year = int(a[0:2])

if b == '1' or b == '2':
    print(112 - year + 1)
else:
    print(12 - year + 1)