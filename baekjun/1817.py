N, M = map(int, input().split())
if N == 0:
    print(0)
else:
    books_weight = list(map(int, input().split()))
    box_cnt = 1
    current_weight = 0
    for book_weight in books_weight:
        current_weight += book_weight
        if current_weight > M:
            current_weight = book_weight
            box_cnt += 1
            continue

    print(box_cnt)