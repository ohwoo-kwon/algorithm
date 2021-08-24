a = input()

a_rev = str(int(a[::-1]) * 2)
a_rev = a_rev[-1:-3:-1]
a_rev = a_rev[::-1]
if a_rev[-2] == '0':
    a_rev = a_rev[-1]
print(a_rev)
if int(a_rev) <= 50:
    print('GOOD')
else:
    print('OH MY GOD')