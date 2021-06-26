n = int(input())
j = 1
stack = []
result = []

for _ in range(n):
    num = int(input())
    while j < num+1:
        stack.append(j)
        result.append('+')
        j += 1
    temp = stack.pop()
    result.append('-')
    if temp != num:
        print('NO')
        break
else:
    for re in result:
        print(re)