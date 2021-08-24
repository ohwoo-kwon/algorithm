N = int(input())
words = []
for n in range(N):
    words += [input()]
result = 0
for word in words:
    for i in range(len(word)):
        indexes = [i]
        checker = True
        for j in range(i+1, len(word)):
            if word[i] == word[j]:
                indexes += [j]
        if len(indexes) != 1:
            for j in range(len(indexes)-1):
                if indexes[j] + 1 != indexes[j+1]:
                    checker = False
                    break
            if checker == False:
                break
    else:
        result += 1
print(result)