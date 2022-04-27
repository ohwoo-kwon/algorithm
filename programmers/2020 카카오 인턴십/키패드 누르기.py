def solution(numbers, hand):
    answer = ''
    keypad = {
        1: (0, 0),
        2: (0, 1),
        3: (0, 2),
        4: (1, 0),
        5: (1, 1),
        6: (1, 2),
        7: (2, 0),
        8: (2, 1),
        9: (2, 2),
        '*': (3, 0),
        0: (3, 1),
        '#': (3, 2),
    }
    curL = '*'
    curR = '#'

    for num in numbers:
        if num in [1, 4, 7]:
            answer += 'L'
            curL = num
        elif num in [3, 6, 9]:
            answer += 'R'
            curR = num
        else:
            disL = abs(keypad[num][0] - keypad[curL][0]) + abs(keypad[num][1] - keypad[curL][1])
            disR = abs(keypad[num][0] - keypad[curR][0]) + abs(keypad[num][1] - keypad[curR][1])
            if disL > disR:
                curR = num
                answer += 'R'
            elif disL < disR:
                curL = num
                answer += 'L'
            else:
                if hand == 'right':
                    curR = num
                    answer += 'R'
                else:
                    curL = num
                    answer += 'L'

    return answer