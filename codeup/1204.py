a = input()

if (a == '11') or (a == '12') or (a == '13'):
    print(a + 'th')
elif (a[-1] == '1'):
    print(a + 'st')
elif (a[-1] == '2'):
    print(a + 'nd')
elif (a[-1] == '3'):
    print(a + 'rd')
else:
    print(a + 'th')