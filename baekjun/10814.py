N = int(input())

members = []
names = []
for i in range(N):
    age, name = input().split()
    members.append([int(age), i])
    names.append(name)

members.sort()

for i in range(N):
    print(members[i][0], names[members[i][1]])