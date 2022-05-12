def solution(phone_book):
    answer = True
    phone_dict = {}
    for phone in phone_book:
        phone_dict[phone] = True

    for phone in phone_book:
        temp = ""
        for i in range(len(phone)):
            temp += phone[i]
            if phone_dict.get(temp) and temp != phone:
                answer = False
                return answer

    return answer


phone_book = ["123", "456", "789", "1234"]
print(solution(phone_book))