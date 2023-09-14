from collections import deque
import sys
inp = sys.stdin.readline

def forceSort(num):
    start = 0
    end = len(dq)-1

    if num <= dq[0]:
        dq.appendleft(num)
    elif num >= dq[-1]:
        dq.append(num)
    else:
        while 1:
            mid = start+end//2
            if dq[mid-1] <= num <= dq[mid]:
                dq.insert(mid, num)
                break
            elif num<dq[mid-1]:
                end = mid-1
            elif dq[mid]<num:
                start == mid
        


N = int(inp().rstrip())

dq = deque()

for _ in range(N):
    if len(dq) == 0:
        dq.append(int(inp()))

    else:
        forceSort(int(inp()))

ansList = list(map(str, dq))
ans = "\n".join(ansList)
print(ans)
