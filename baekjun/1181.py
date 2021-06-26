N = int(input())

words = []
for i in range(N):
    word = input()
    words.append([len(word), word])

words.sort()
i = 0

while i < N:
    if i == N-1:
        print(words[i][1])
        break
    elif words[i] == words[i+1]:
        j = 1
        while i+j < N and words[i] == words[i+j]:
            j += 1
        print(words[i][1])
        i += j
    else:
        print(words[i][1])
        i += 1