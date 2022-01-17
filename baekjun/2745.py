N, B = input().split()

result = 0
for i in range(len(N)):
    if ord(N[i]) < 58:
        result += (ord(N[i]) - 48) * (int(B) ** (len(N) - 1 - i))
    else:
        result += (ord(N[i]) - 55) * (int(B) ** (len(N) - 1 - i))
print(result)