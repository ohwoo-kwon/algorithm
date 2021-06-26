a, b, c = input().split()

if (int(b) < 10) & (int(c) >= 100):
    print(a + '0' + b + c)
elif (int(b) < 10) & (10 <= int(c) < 100):
    print(a + '0' + b + '0' + c)
elif (int(b) < 10) & (int(c) < 10):
    print(a + '0' + b + '00' + c)
elif (int(b) >= 10) & (int(c) >= 100):
    print(a + b + c)
elif (int(b) >= 10) & (10 <= int(c) < 100):
    print(a + b + '0' + c)
else:
    print(a + b + '00' + c)