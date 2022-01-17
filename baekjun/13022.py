# 먼저 w의 갯수를 체크한다
# w 가 아니면 o, l, f 순서대로 w의 갯수만큼 연속으로 존재하는지 확인
# 존재하면 1 아니면 0 출력
def check_word(wolf, idx, w_cnt, now):
    for i in range(idx, idx+w_cnt):
        if i >= len(wolf) or now != wolf[i]:
            return False
    return True

wolf = input()

w_cnt = 0
idx = 0
now = wolf[idx]
result = 1

if now != "w":
    result = 0
else:
    while idx < len(wolf):
        if wolf[idx] == "w":
            w_cnt += 1
            idx += 1
            now = "w"
        else:
            if now == "w" and wolf[idx] != "o":
                result = 0
                break
            elif now == "o" and wolf[idx] != "l":
                result = 0
                break
            elif now == "l" and wolf[idx] != "f":
                result = 0
                break
            elif now == "f" and wolf[idx] != "w":
                result = 0
                break
            now = wolf[idx]
            is_ok = check_word(wolf, idx, w_cnt, now)
            if not is_ok:
                result = 0
                break
            idx += w_cnt
            if now == "f":
                w_cnt = 0
if now != "f":
    result = 0
print(result)