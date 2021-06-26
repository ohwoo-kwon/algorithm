cro = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

words = input()
length = len(words)
result = 0
word = [words]
i = 0
j = 0

while i < len(cro):
    if cro[i] in word[j]:
        word += [word[j].replace(cro[i],'a', 1)]
        j += 1
        result += 1
    else:
        i += 1
print(len(word[-1]))