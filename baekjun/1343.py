question = input()
cnt = 0
result = ""
for i in range(len(question)):
    if question[i] == ".":
        if cnt != 2 and cnt != 4 and cnt != 0:
            result = -1
            break
        if cnt == 4:
            result += "AAAA"
            cnt = 0
        elif cnt == 2:
            result += "BB"
            cnt = 0
        result += "."
        continue
    cnt += 1
    if cnt == 4:
        result += "AAAA"
        cnt = 0
else:
    if cnt == 2:
        result += "BB"
    elif cnt == 0:
        result += ""
    else:
        result = -1

print(result)
