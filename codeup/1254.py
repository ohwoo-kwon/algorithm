a1, a2 = input().split()

a1 = ord(a1)
a2 = ord(a2)

a_list = []
for i in range(a1, a2 +1):
    a_list.append(i)

for i in a_list:
    print(chr(i), end=' ')