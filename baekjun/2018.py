N = int(input())
result = 1

start_num = 1
end_num = 2
sum_nums = 3

while start_num <= N//2:
    if sum_nums < N:
        end_num += 1
        sum_nums += end_num
    elif sum_nums > N:
        sum_nums -= start_num
        start_num += 1
    else:
        result += 1
        end_num += 1
        sum_nums += end_num
        sum_nums -= start_num
        start_num += 1

print(result)