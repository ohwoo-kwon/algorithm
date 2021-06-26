N = int(input())
count = 99
if N < 100:
    print(N)
else:
    for n in range(100, N+1):
        list_nums = list(map(int, str(n)))
        for i in range(len(list_nums)-2):
            if list_nums[i+1] - list_nums[i] == list_nums[i+2] - list_nums[i+1]:
                continue
            else:
                break
        else:
            count += 1
    print(count)