a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)

if b > a:
    if b > c:
        if b < a + c:
            print('yes')
        else:
            print('no')
    else:
        if c < a + b:
            print('yes')
        else:
            print('no')
elif c > a:
    if c < a + b:
        print('yes')
    else:
        print('no')
else:
    if a < b + c:
        print('yes')
    else:
        print('no')
