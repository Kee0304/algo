from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
ans = 0
dq = deque([N])
def check(num):
    global ans
    if num == 1:
        return True
    else:
        dq.append(num)
        return False

def BFS():
    global ans
    while dq:
        for _ in range(len(dq)):
            cur = dq.popleft()
            if cur%3 == 0:
                next = N//3
                if check(next) == True:
                    return
            
            if cur%2 == 0:
                next = N//2
                if check(next) == True:
                    return
            
            if cur > 1:
                next = cur-1
                if check(next) == True:
                    return
            
        ans += 1

BFS()
print(ans)

