def solution(genres, plays):
    answer = []
    info_dict = {}
    for i in range(len(genres)):
        if info_dict.get(genres[i]):
            info_dict[genres[i]][0] += plays[i]
            info_dict[genres[i]][1].append([plays[i], i])
        else:
            info_dict[genres[i]] = [plays[i], [[plays[i], i]]]
    values = info_dict.values()
    sorted_values = sorted(values, reverse=True)
    for value in sorted_values:
        print(value[1])
        value[1].sort(key=lambda x: x[1])
        print(value[1])
        value[1].sort(key=lambda x: x[0])
        print(value[1])
        for i in range(len(value[1])):
            if i == 2:
                break;
            answer.append(value[1][i][1])

    return answer