import sys
from itertools import combinations
from math import sqrt
inp = sys.stdin.readline

T = int(inp())

for _ in range(T):
    ans = 200000*20
    # 점의 개수(항상 짝수)
    N = int(inp())
    posList = [None for _ in range(N)]
    allX = 0
    allY = 0
    for i in range(N):
        inputTuple = tuple(map(int,inp().split()))
        allX += inputTuple[0]
        allY += inputTuple[1]
        posList[i] = inputTuple
    
    startPosList = list(combinations(range(N),N//2))

    for startPos in startPosList[:len(startPosList)//2]:
        sumX = 0
        sumY = 0
        for i in startPos:
            sumX += posList[i][0]
            sumY += posList[i][1]

        sumX -= (allX - sumX)
        sumY -= (allY - sumY)
        partVectorSum  = sqrt(sumX**2+sumY**2)

        if ans > partVectorSum:
            ans = partVectorSum

    print(ans)        