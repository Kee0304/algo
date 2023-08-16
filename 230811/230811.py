from collections import deque
import sys
inp = sys.stdin.readline

N, K = inp().split()
numberList = list(map(int,list(N)))
intofK = int(K)

def solve(intK):
    length = len(numberList)
    if length == 1 or (length == 2 and numberList.count(0) == 1):
        return -1
    
    else:
        ans = 0
        dq = deque()
        dq.append(numberList)
        while intK >= 1:
            if dq:
                visited = set()
                for _ in range(len(dq)):
                    cur = dq.popleft()
                    for i in range(length):
                        for j in range(i+1, length):
                            newList = cur[:]
                            newList[i], newList[j] = newList[j], newList[i]
                            if newList[0] != 0 and (tuple(newList) not in visited):
                                dq.append(newList)
                                visited.add(tuple(newList))
                intK -= 1

            else:
                return -1
            
        for numList in dq:
            num = int("".join(map(str,numList)))
            if ans < num:
                ans = num
        
        return ans

print(solve(intofK))