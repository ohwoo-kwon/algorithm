N, K = map(int, input().split())

result = 0
std_time = N*60*60 + 59*60 + 60

for time in range(std_time):
    h = time // 3600
    time %= 3600
    m = time // 60
    time %= 60

    if h < 10:
        h = "0" + str(h)
    elif m < 10:
        m = "0" + str(m)
    elif time < 10:
        time = "0" + str(time)
    temp = str(h) + str(m) + str(time)
    if str(K) in temp:
        result += 1

print(result)