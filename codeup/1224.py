a, b, c, d = input().split()
a = int(a)
b = int(b)
c = int(c)
d = int(d)

div1 = a / b
div2 = c / d

if div1 > div2:
    print('>')
elif div2 > div1:
    print('<')
else:
    print('=')