M = int(input())
N = int(input())

is_prime_num = [True] * (N+1)
is_prime_num[0], is_prime_num[1] = False, False

for num in range(2, int(N**0.5)+1):
    if is_prime_num[num]:
        temp = num + num
        while temp <= N:
            is_prime_num[temp] = False
            temp += num


sum_primes = 0
min_value = 0
flag = False
for i in range(M, N+1):
    if is_prime_num[i]:
        sum_primes += i
        if not flag:
            min_value = i
            flag = True

if min_value:
    print(sum_primes)
    print(min_value)
else:
    print(-1)