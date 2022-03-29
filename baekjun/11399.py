N = int(input())
withdrawal_times = list(map(int, input().split()))

withdrawal_times.sort()

for i in range(1, N):
    withdrawal_times[i] += withdrawal_times[i-1]

print(sum(withdrawal_times))