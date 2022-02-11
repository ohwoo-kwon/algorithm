# 개강총회 시작 한 시간 전과 시작하자마자 채팅 기록 -> 입장
# 개총 끝 ~ 스트리밍 끝 채팅 기록 -> 퇴장

# 출석한 인원을 넣는 리스트
# 출석한 사람 중 퇴장한 사람 있으면 result + 1
import sys

def htom(time):
    h, m = map(int, time.split(":"))
    return h * 60 + m


S, E, Q = input().split()
S = htom(S)
E = htom(E)
Q = htom(Q)

participant_list = set()
result = 0

while True:
    try:
        time, name = sys.stdin.readline().split()
        if htom(time) <= S:
            participant_list.add(name)
        elif E <= htom(time) <= Q and name in participant_list:
            participant_list.remove(name)
            result += 1
    except:
        break

print(result)