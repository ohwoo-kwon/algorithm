import sys
input = sys.stdin.readline

def to_one(num):
    visited = [False] * 487

    while True:
        result = 0
        while num:
            temp = num % 10
            num //= 10
            result += temp ** 2
        if result == 1: return True
        if visited[result]: return False
        num = result
        visited[num] = True


n = int(input())

# n 보다 작은 소수 찾기
prime = [True] * (n+1)
prime[0] = prime[1] = False
for i in range(2, n+1):
    if prime[i]:
        for j in range(2, n//i + 1):
            prime[i*j] = False

# 소수 중에서 상근수 찾기
for i in range(2, n+1):
    if prime[i]:
        res = to_one(i)
        if res:
            print(i)
