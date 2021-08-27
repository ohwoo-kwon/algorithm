def power(A, B, C):
    if B == 1:
        return A % C
    else:
        tmp = power(A, B//2, C)
        if B % 2: # B가 홀수인 경우
            return tmp * tmp * A % C
        else:
            return tmp * tmp % C

A, B, C = map(int, input().split())

result = power(A, B, C)
print(result)