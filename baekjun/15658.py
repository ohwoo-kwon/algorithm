def Caculator(value, num, i):
    if i == 0:
        value += num
    elif i == 1:
        value -= num
    elif i == 2:
        value *= num
    else:
        if value >= 0:
            value //= num
        else:
            value = -value
            value //= num
            value = -value
    return value

def Greedy(n, N, value):
    if n >= N:
        global max_v
        global min_v
        max_v = max(max_v, value)
        min_v = min(min_v, value)
        return

    for i in range(4):
        if operators[i] > 0:
            operators[i] -= 1
            temp = Caculator(value, nums[n], i)
            Greedy(n+1, N, temp)
            operators[i] += 1

N = int(input())
nums = list(map(int, input().split()))
operators = list(map(int, input().split()))

max_v = -1000000001
min_v = 1000000001

Greedy(1, N, nums[0])

print(max_v)
print(min_v)