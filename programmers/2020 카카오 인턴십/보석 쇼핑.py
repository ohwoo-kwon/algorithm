def solution(gems):
    answer = []
    shortest = len(gems) + 1
    start = end = 0
    check = len(set(gems))
    contain = {}

    while end < len(gems):
        if gems[end] not in contain:
            contain[gems[end]] = 1
        else:
            contain[gems[end]] += 1
        end += 1
        if len(contain) == check:
            while start < end:
                if contain[gems[start]] > 1:
                    contain[gems[start]] -= 1
                    start += 1
                elif shortest > end - start:
                    shortest = end - start
                    answer = [start + 1, end]
                    break
                else:
                    break
    return answer