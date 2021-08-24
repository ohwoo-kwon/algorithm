a,b = input().split()

a = float(a)
b = float(b)
values = [a+b, a-b, b-a, a*b, a/b, b/a, a**b, b**a]
max_value = values[0]

for value in values:
    if value > max_value:
        max_value = value

print('%.6f' % max_value)