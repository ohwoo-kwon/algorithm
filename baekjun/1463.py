N = int(input())

post_result = [0] * 10000001
post_result[2] = 1
post_result[3] = 1

for i in range(4, N+1):
    if i % 6 == 0:
        a = post_result[i // 3] + 1
        b = post_result[i - 1] + 1
        c = post_result[i // 2] + 1
        post_result[i] = min(a, b, c)
    elif i % 3 == 0:
        a = post_result[i//3] + 1
        b = post_result[i-1] + 1
        post_result[i] = min(a, b)
    elif i % 2 == 0:
        a = post_result[i//2] + 1
        b = post_result[i-1] + 1
        post_result[i] = min(a, b)
    else:
        post_result[i] = post_result[i-1] + 1

print(post_result[N])