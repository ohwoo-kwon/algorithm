import sys
input = sys.stdin.readline

N = int(input())
participants = dict()

for _ in range(N):
    name = input()

    if name in participants.keys():
        participants[name] += 1
    else:
        participants[name] = 1

for _ in range(N-1):
    name = input()
    if name in participants.keys():
        participants[name] -= 1

for key, value in participants.items():
    if value:
        print(key)