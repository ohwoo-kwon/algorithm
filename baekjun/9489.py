while True:
    n, k = map(int, input().split())
    if not n and not k: break

    nums = list(map(int, input().split()))
    p = [0] * n
    x = 0
    idx = 0
    for i in range(1, n):
        if nums[i] == k: idx = i
        if nums[i-1] + 1 != nums[i]:
            x += 1
        p[i] = x

    result = 0
    for i in range(n):
        if p[i] != p[idx] and p[p[i]-1] == p[p[idx]-1]: result += 1
    print(result)