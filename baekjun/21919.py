def is_prime(n):
    for i in range(2, int(n ** 0.5)+1):
        if n % i == 0:
            return False
    return True

N = int(input())
A = list(map(int, input().split()))
prime_nums = set()
for num in A:
    if is_prime(num):
        prime_nums.add(num)

result = 1
for prime in prime_nums:
    result *= prime

print(-1 if result == 1 else result)