N = int(input())
times = [list(map(int, input().split())) for _ in range(N)]

times = sorted(times, key=lambda time:(time[1], time[0]))
end = 0
result = 0
for time in times:
    s, e = time
    if end <= s:
        end = e
        result += 1

print(result)