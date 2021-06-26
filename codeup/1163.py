y, m, d = map(int, input().split())

saju = (y + m + d) // 10 //10 % 10

if saju % 2:
    print('그럭저럭')
else:
    print('대박')