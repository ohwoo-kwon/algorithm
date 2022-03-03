word = list(input())
answer = []

for i in range(1, len(word) -1):
    for j in range(i+1, len(word)):
        first = word[:i]
        second = word[i:j]
        third = word[j:]
        first.reverse()
        second.reverse()
        third.reverse()
        answer.append("".join(first + second + third))

print(sorted(answer)[0])