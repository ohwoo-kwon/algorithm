a, b = map(int, input().split())

if a % 2 == 1:
    print('홀수+', end='')
    if b % 2 == 1:
        print('홀수=짝수', end='')
    else:
        print('짝수=홀수', end='')
else:
    print('짝수+', end='')
    if b % 2 == 1:
        print('홀수=홀수', end='')
    else:
        print('짝수=짝수', end='')
