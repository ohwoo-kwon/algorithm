nums = list(map(int, input().split()))
n = min(nums)

while True:
    cnt = 0
    for num in nums:
        if n % num == 0:
            cnt +=1
    if cnt >= 3:
        print(n)
        break
    n += 1