n = int(input())
pibo = [0] * 91
pibo[1] = 1

for i in range(2, n+1):
    pibo[i] = pibo[i-1] + pibo[i-2]

print(pibo[n])