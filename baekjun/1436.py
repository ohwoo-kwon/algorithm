# 666, 1666, 2666 ... 6666, 6667, 6668, 6669, 9666, 10666, 11666 ... 16666, 16667, 16668, 16669, 17666, 18666
# 19666, 20666,

def FinishNum(N):
    cnt = 0
    while N > 0 and cnt != 3:
        if N % 10 == 6:
            cnt += 1
        else:
            cnt = 0
        N //= 10
    if cnt == 3:
        return True
    else:
        return False

N = int(input())
numbers = []
i = 666
while len(numbers) < N:
    if FinishNum(i):
        numbers += [i]
        i += 1
    else:
        i += 1
        continue

print(numbers[N-1])