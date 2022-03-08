def get_divide_num(num):
    result = []
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            result.append(i)
            result.append(num//i)
    return list(set(result))



N = int(input())
nums = list(map(int, input().split()))
max_num = max(nums)
X = int(input())
divide_nums = get_divide_num(X)
answer = 0
cnt = 0
for num in nums:
    for divide_num in divide_nums:
        if num % divide_num == 0:
            break
    else:
        answer += num
        cnt += 1

print(answer / cnt)