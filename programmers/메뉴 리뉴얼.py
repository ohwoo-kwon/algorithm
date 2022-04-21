import itertools
import collections

def solution(orders, course):
    answer = []
    for size in course:
        order_combinations = []
        for order in orders:
            order_combinations += itertools.combinations(sorted(order), size)
        most_ordered = collections.Counter(order_combinations).most_common()
        for k, v in most_ordered:
            if v > 1 and v == most_ordered[0][1]:
                answer.append(''.join(k))
    answer.sort()
    return answer