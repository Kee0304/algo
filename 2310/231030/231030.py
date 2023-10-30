import sys
input = sys.stdin.readline

N = int(input().rstrip())
lst = list(map(int,input().split()))

pList = []
for i in range(N):
    if i < N-1:
        if i == 0:
            pList.append(i)
            if lst[i] > lst[i+1]:
                pList.append(i+1)
        
        else:
            if lst[i] > lst[i+1]:
                pList.append(i)
                pList.append(i+1)

ans = 0
for p in pList:
    tempList = []
    for i in range(p, N):
        if i == p:
            tempList.append(lst[i])
        else:
            if len(tempList)>=2:
                for j in range(len(tempList)-1, 0, -1):
                    if tempList[j] > lst[i] and tempList[0] < lst[i]:
                        tempList=tempList[:j]
                        if tempList[-1] == lst[i]:
                            pass
                        else:
                            tempList.append(lst[i])
                else:
                    if tempList[-1] < lst[i]:
                        tempList.append(lst[i])
            else:
                if tempList[0] < lst[i]:
                    tempList.append(lst[i])
        
        print(tempList)
        tLen = len(tempList)
        if ans < tLen:
            ans = tLen

print(ans)