def Perm(idx, start):
    if idx == N//2:
        s1, s2 = Stat()
        diff.append(abs(s1 - s2))
        return
    if idx == 0:
        teamA.append(0)
        teamB.remove(0)
        Perm(idx+1, 1)
    else:
        for i in range(start, N):
            teamA.append(i)
            teamB.remove(i)
            Perm(idx+1, i+1)
            teamA.remove(i)
            teamB.append(i)

def Stat():
    s1 = 0
    s2 = 0
    for i in range(N//2):
        for j in range(i+1, N//2):
            s1 += S[teamA[i]][teamA[j]]
            s1 += S[teamA[j]][teamA[i]]
            s2 += S[teamB[i]][teamB[j]]
            s2 += S[teamB[j]][teamB[i]]
    return s1, s2

N = int(input())
S = [list(map(int, input().split())) for _ in range(N)]

diff = []
teamA = []
teamB = []
for i in range(N):
    teamB.append(i)

Perm(0, 0)

print(min(diff))