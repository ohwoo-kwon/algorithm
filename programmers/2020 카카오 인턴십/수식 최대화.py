import itertools

def split_expression(expression):
    result = []
    temp = ""
    for i in range(len(expression)):
        if expression[i].isdigit():
            temp += expression[i]
        else:
            result.append(temp)
            result.append(expression[i])
            temp = ""
    result.append(temp)
    return result


def solution(expression):
    operators = list(itertools.permutations(["-", "+", "*"], 3))
    answer = 0
    results = []
    for operator in operators:
        splited = split_expression(expression)
        for op in operator:
            while op in splited:
                idx = splited.index(op)
                print(splited[idx-1] + op + splited[idx+1])
                print(eval(splited[idx-1] + op + splited[idx+1]))
                splited[idx-1] = str(eval(splited[idx-1] + op + splited[idx+1]))
                del splited[idx:idx+2]
        results.append(abs(int(splited[0])))
    return max(results)