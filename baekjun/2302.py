N = int(input())
M = int(input())
vip = []
for _ in range(M):
    vip.append(int(input()))

seat = [1, 1, 2]
for i in range(3, N+1):
    seat.append(seat[i-1] + seat[i-2])

result = 1
if M >= 1:
    temp = 0
    for i in range(M):
        result *= seat[vip[i]-1-temp]
        temp = vip[i]
    result *= seat[N-temp]
    print(result)
else: print(seat[N])