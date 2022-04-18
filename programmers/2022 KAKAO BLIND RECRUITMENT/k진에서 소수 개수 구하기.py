def ten_to_k(n, k):
    nums = []
    while n > 0:
        nums.append(str(n % k))
        n //= k
    nums.reverse()
    return ''.join(nums)


def is_prime(prime_num, n):
    n = int(n)
    if n == 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    prime_num[n] = True
    return True


def solution(n, k):
    answer = 0
    n_to_k = ten_to_k(n, k)
    prime_num = {}

    nums = n_to_k.split("0")
    for num in nums:
        if num == '':
            continue
        if prime_num.get(num):
            continue
        if is_prime(prime_num, num):
            answer += 1
    return answer