a, b, c, d = input().split()

sticks = [a, b, c, d]

stick = sticks.count('1')

if stick == 1:
    print('도')
elif stick == 2:
    print('개')
elif stick == 3:
    print('걸')
elif stick == 4:
    print('윷')
else:
    print('모')