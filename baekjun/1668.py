N = int(input())

l_cnt = 0
r_cnt = 0
l_max = 0
r_max = 0
prizes = []

for _ in range(N):
    t = int(input())
    prizes.append(t)
    if t > l_max:
        l_max = t
        l_cnt += 1
print(l_cnt)

for i in range(N-1, -1, -1):
    if prizes[i] > r_max:
        r_max = prizes[i]
        r_cnt += 1
print(r_cnt)