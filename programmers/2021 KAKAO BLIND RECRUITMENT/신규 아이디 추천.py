import re

def solution(new_id):
    # 1단계 : 소문자 치환
    new_id = new_id.lower()
    # 2단계 : 가능 문자 제외 제거
    new_id = re.sub(r"[^a-z0-9\-\_\.]","",new_id)
    # 3단계 : . 연속 시 중복 제거
    new_id = re.sub(r"[\.]+", ".", new_id)
    # 4단계 : 마침표가 처음이나 끝일 시 제거
    if new_id.startswith('.'): new_id = new_id[1:]
    if new_id.endswith('.'): new_id = new_id[:-1]
    # 5단계 : 빈 문자열 a 대입
    if new_id == '': new_id = 'a'
    # 6단계 : 16자 이상
    if len(new_id) >= 16:
        new_id = new_id[:15]
        if new_id.endswith('.'):
            new_id = new_id[:-1]
    if len(new_id) < 3:
        while len(new_id) < 3:
            new_id += new_id[-1]

    return new_id