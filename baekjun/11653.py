N = int(input())
n = 2
while N > 1:
    if N % n:
        n += 1
        continue
    else:
        print(n)
        N //= n