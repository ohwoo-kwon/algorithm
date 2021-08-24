a, b = input().split()
a = float(a)
b = float(b)

while (a -b) < 1e-10:
    print('%.2f' %a, end=' ')
    a += 0.01