def ston(word):
    nums = {
        'zero': '0',
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9',
    }
    if not nums.get(word): return False
    return nums[word]

def solution(s):
    answer = ''
    temp = ''
    for char in s:
        if char.isdigit():
            answer += char
        else:
            temp += char
        num = ston(temp)
        if num:
            answer += num
            temp = ''
    return int(answer)