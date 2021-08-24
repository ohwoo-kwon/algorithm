a, b = input().split()

a_reverse = ''
b_reverse = ''
for i in range(2,-1,-1):
    a_reverse += a[i]
    b_reverse += b[i]

if int(a_reverse) > int(b_reverse):
    print(a_reverse)
else:
    print(b_reverse)