def Perm(idx):
    global cnt
    if idx == N:
        cnt += 1
        return
    for i in range(N):
        stack[idx] = i
        if Able(idx):
            Perm(idx+1)

def Able(idx):
    for i in range(idx):
        if stack[i] == stack[idx] or abs(stack[i] - stack[idx]) == idx - i:
            return False
    return True

N = int(input())

cnt = 0
stack = [0] * N
Perm(0)
print(cnt)