class Node:
    def __init__(self):
        self.removed = False
        self.prev = None
        self.next = None


def solution(n, k, cmd):
    nodeArr = [Node() for _ in range(n)]
    for i in range(1, n):
        nodeArr[i - 1].next = nodeArr[i]
        nodeArr[i].prev = nodeArr[i - 1]

    curr = nodeArr[k]
    deleted = []

    for get_cmd in cmd:
        if get_cmd[0] == 'U':
            x = int(get_cmd[2:])
            for _ in range(x):
                curr = curr.prev
        elif get_cmd[0] == 'D':
            x = int(get_cmd[2:])
            for _ in range(x):
                curr = curr.next
        elif get_cmd[0] == 'C':
            deleted.append(curr)
            curr.removed = True
            up = curr.prev
            down = curr.next
            if up:
                up.next = down
            if down:
                down.prev = up
                curr = down
            else:
                curr = up
        else:
            node = deleted.pop()
            node.removed = False
            up = node.prev
            down = node.next
            if up:
                up.next = node
            if down:
                down.prev = node

    answer = ''
    for i in range(n):
        if nodeArr[i].removed:
            answer += 'X'
        else:
            answer += 'O'

    return answer