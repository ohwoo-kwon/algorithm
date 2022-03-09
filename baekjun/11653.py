N = int(input())
i = 2
while N > 1:
    if not N % i:
        print(i)
        N //= i
        continue
    else:
        i += 1