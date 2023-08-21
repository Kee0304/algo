from string import ascii_uppercase
from pprint import pprint
import sys
inp = sys.stdin.readline

alplist = list(ascii_uppercase)
tsList = []
N = int(inp())
maxlen = 0
for _ in range(N):
    inpStr = inp().rstrip()
    strLength = len(inpStr)
    if strLength > maxlen:
        maxlen = strLength
    zfillList = list(inpStr.zfill(50))
    tsList.append(zfillList)

K = int(inp())
ans = 0

pprint(tsList,width= 300)

startIndex = 50 - maxlen
curIndex = startIndex

def changeNumber(curIndex):
    global K

    if K == 0:
        return

    for row in range(N):
        indexList = ['0' for _ in range(N)]
        # 각 row의 현재 index 값 저장
        indexList[row] = tsList[row][curIndex]
        # 만약 현재가 시작 인덱스면
        if curIndex == startIndex:
            cnt = 0
            while cnt < N:
                minStr = 'Z'
                minIndex = 0
                for loopIndex in range(N):
                    # 0은 건드릴 필요가 없다
                    if indexList[loopIndex] == '0':
                        cnt +=1
                    else:
                        # 최솟값 갱신
                        if indexList[loopIndex] < minStr:
                            minStr = indexList[loopIndex]
                            minIndex = loopIndex
                    # 가장 작은 놈 Z로 갱신하고 K-=1
                    if tsList[row][curIndex] == minStr and minStr != 'Z':
                        tsList[row][curIndex] = 'Z'
                        indexList[minIndex] = 'Z'
                        K -= 1
                        cnt+=1
                        # K가 0이면 그만
                        if K == 0:
                            return