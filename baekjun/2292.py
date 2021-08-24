N = int(input())
end = 2
i = 0

if N == 1:
    print(1)
else:
    while N >= end:
        end += 6*i
        i += 1
    print(i)