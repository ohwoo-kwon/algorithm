n_sen = input()
key_sen = input()

result = ""

i = j = 0
while i < len(n_sen):
    i %= len(n_sen)
    j %= len(key_sen)

    if n_sen[i] != " ":
        a_ord = ord(key_sen[j]) - ord("a") + 1
        new_ord = ord(n_sen[i]) - a_ord
        if new_ord < ord("a"):
            new_ord = ord("z") - (ord("a") - new_ord) + 1
        result += chr(new_ord)
    else: result += " "
    i += 1
    j += 1

print(result)