N = int(input())
wines = [0] * (N+1)
for i in range(1, N+1):
    wines[i] = int(input())

wines_result = [0]
wines_result.append(wines[1])

if N > 1:
    wines_result.append(wines[2]+wines[1])

for i in range(3, N+1):
    wines_result.append(max(wines_result[i-1],wines_result[i-3]+wines[i-1]+wines[i], wines_result[i-2]+wines[i]))

print(wines_result[N])