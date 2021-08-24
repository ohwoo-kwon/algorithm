sosu = [0] * 100001
sosu[0] = 1
sosu[1] = 1
for i in range(2, int(100001**0.5)+1):
    for j in range(2*i, 100001, i):
        if sosu[j] == 0:
            sosu[j] = 1

for t in range(1, int(input())+1):
    N = int(input())
    n = N//2
    while True:
        if sosu[n] == 0:
            a = n
            b = N - a
            if sosu[b] == 0:
                break
        n += 1
    print(b, a)