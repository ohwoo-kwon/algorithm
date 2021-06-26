a, b, c = input().split()

if int(c) >= 10:
    print(a + b + c)
else:
    print(a + b + '0' + c)