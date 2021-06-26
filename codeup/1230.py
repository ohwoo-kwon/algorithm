a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)
if(a <= 170):
    print('CRASH ' + str(a))
elif(b <= 170):
    print('CRASH ' + str(b))
elif(c <= 170):
    print('CRASH ' + str(c))
else:
    print('PASS')