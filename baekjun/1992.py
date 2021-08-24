def Split(rs, re, cs, ce): # rs, re : 행의 시작과 끝 / cs, ce : 열의 시작과 끝
    ms = (rs+re)//2
    mc = (cs+ce)//2
    isfinish = False
    i = videos[rs][cs]
    for r in range(rs, re+1):
        for c in range(cs, ce+1):
            if videos[r][c] != i:
                isfinish = True
                break
        if isfinish:
            break
    else: # break를 안타면(즉, 모든 숫자가 같으면) 해당 숫자를 출력
        print(i, end='')
        return

    print('(', end='')
    Split(rs, ms, cs, mc)
    Split(rs, ms, mc+1, ce)
    Split(ms+1, re, cs, mc)
    Split(ms+1, re, mc+1, ce)
    print(')', end='')


N = int(input())
videos = [list(input()) for _ in range(N)]

Split(0, N-1, 0, N-1)