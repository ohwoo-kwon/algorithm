y, m, d = map(int, input().split())

saju = y - m + d

if saju % 10 == 0:
    print('대박')
else:
    print('그럭저럭')