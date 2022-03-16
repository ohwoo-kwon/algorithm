def GCD(a, b):
    while b:
        c = a % b
        a = b
        b = c
    return a


for _ in range(int(input())):
    a, b = map(int, input().split())

    c = GCD(a, b)

    print(a*b//c)