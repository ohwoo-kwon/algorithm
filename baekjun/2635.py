N = int(input())
result = 0
nums = []
for num in range(N+1):
    cnt = 2
    temp = [N, num]
    front_num = N
    back_num = num
    n = front_num - back_num
    while n >= 0:
        cnt += 1
        temp.append(n)
        front_num = back_num
        back_num = n
        n = front_num - back_num

    if cnt > result:
        result = cnt
        nums = temp

print(result)
print(*nums)
