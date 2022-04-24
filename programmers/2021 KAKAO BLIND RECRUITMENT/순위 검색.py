import bisect


def solution(info, query):
    answer = []
    info_dict = {}

    temp = []

    for person in info:
        person = person.split()
        k, score = tuple(person[:-1]), int(person[-1])
        temp.append((k, score))

    temp.sort(key=lambda x: x[1])

    for item in temp:
        k, score = item
        if k not in info_dict:
            info_dict[k] = []
        info_dict[k].append(score)

    for q in query:
        q = q.split()
        q = list(filter(lambda x: x != 'and', q))
        q_score = int(q[-1])
        q = q[:-1]
        print(q)

        q_k = list(info_dict.keys())

        for current_q in q:
            if current_q == '-':
                continue
            q_k = list(filter(lambda x: current_q in x, q_k))

        q_infos = [info_dict[x] for x in q_k]
        cnt = 0
        for scores in q_infos:
            idx = bisect.bisect_left(scores, q_score)
            i = len(scores) - idx
            cnt += i
        answer.append(cnt)

    return answer