def solution(id_list, report, k):
    answer = []
    block_me = {}
    cnt_list = {}

    for my_id in id_list:
        block_me[my_id] = []
        cnt_list[my_id] = 0

    for info in report:
        you, me = info.split(" ")
        if you in block_me[me]:
            continue
        block_me[me].append(you)

    for my_id, values in block_me.items():
        if len(values) >= k:
            for your_id in values:
                cnt_list[your_id] += 1

    for my_id in id_list:
        answer.append(cnt_list[my_id])

    return answer