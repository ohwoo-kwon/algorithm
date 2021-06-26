a, b, c = input().split()

a = int(a)
b = int(b)
c = int(c)

if a > b:
    if a > c:
        if b > c:
            second = b
        else:
            second = c
    else:
        second = a
else:
    if b > c:
        if a > c:
            second = a
        else:
            second = c
    else:
        second = b

print(second)
