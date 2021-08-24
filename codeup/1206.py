a, b = input().split()
a = int(a)
b = int(b)

if b % a == 0:
    print(f'{a}*{b//a}={b}')
elif a % b == 0:
    print(f'{b}*{a//b}={a}')
else:
    print('none')