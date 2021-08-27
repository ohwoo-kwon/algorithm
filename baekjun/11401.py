N, K = map(int, input().split())
p = 1000000007

def power(a, b):
    if b == 0:
        return 1
    elif b % 2:
        return power(a, b//2) ** 2 * a % p
    else:
        return power(a, b//2) ** 2 % p

fac = [1] * (N+1)

for i in range(2, N+1):
    fac[i] = i * fac[i-1] % p

A = fac[N] % p
B = fac[K] * fac[N-K] % p

print((A * (power(B, p-2) % p)) % p)