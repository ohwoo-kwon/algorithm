def perm(cnt, cur, idx, values, result):
    if cnt <= cur:
        global answer
        answer += result
        return

    for i in range(idx, len(values)):
        result *= values[i]
        perm(cnt, cur + 1, i+1, values, result)
        result //= values[i]


def solution(clothes):
    global answer
    answer = 0
    clothes_object = {}
    for cloth in clothes:
        if clothes_object.get(cloth[1]):
            clothes_object[cloth[1]] += 1
        else:
            clothes_object[cloth[1]] = 1

    values = list(clothes_object.values())
    for cnt in range(1, len(values) + 1):
        perm(cnt, 0, 0, values, 1)

    return answer

print(solution([["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]))
