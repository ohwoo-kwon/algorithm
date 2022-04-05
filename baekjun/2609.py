a, b = map(int, input().split())

if a < b:
    m, n = b, a
else:
    m, n = a, b

while n > 0:
    temp = m % n
    m = n
    n = temp

print(m)
print(m * (a//m) * (b//m))