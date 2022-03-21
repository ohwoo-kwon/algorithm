def make_team(cnt, start, team_start, team_link):
    if cnt == N//2:
        team_start_score = 0
        team_link_score = 0

        for i in range(N//2):
            for j in range(i+1, N//2):
                team_start_score += S[team_start[i]][team_start[j]]
                team_start_score += S[team_start[j]][team_start[i]]
                team_link_score += S[team_link[i]][team_link[j]]
                team_link_score += S[team_link[j]][team_link[i]]

        results.append(abs(team_start_score - team_link_score))
        return

    if cnt == 0:
        team_start.append(0)
        team_link.remove(0)
        make_team(cnt+1, 1, team_start, team_link)
        return

    for member in range(start, N):
        team_start.append(member)
        team_link.remove(member)
        make_team(cnt+1, member+1, team_start, team_link)
        team_start.remove(member)
        team_link.append(member)


N = int(input())
S = []
for _ in range(N):
    S.append(list(map(int, input().split())))

results = []

make_team(0, 0, [], [i for i in range(N)])
print(min(results))