S = list(input())
result = [0] * 26

for alphabet in S:
    result[ord(alphabet) - 97] += 1

print(*result)