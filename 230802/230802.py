from collections import deque

import sys

inp = sys.stdin.readline

#X, Y, D, T = map(int,inp().split())
X = 6
Y = 8
D = 5
T = 3

oneStepDrow = [-1,0,1,0]
oneStepDcol = [0,1,0,-1]

jumpDrow = [-D,0,D,0]
jumpDcol = [0,D,0,-D]

sec = 0

# T초 동안 직선으로 D만큼 이동했을 때 남은 거리가
# T초 동안 최단 거리로 T만큼 이동했을 때 남은 거리보다 크면 점프, 아니면 걷기
cur = [X,Y]
cursec = 0
# 집 기준 1사분면에 있으면

while 1:
    print(f'현재 위치는 {cur[0],cur[1]}, 현재 초는 {cursec}')
    jsec = cursec
    ssec = cursec
    rjumpmindis = 1000000000000000
    newRow = cur[0]
    newCol = cur[1]
    jumpPos = [cur[0], cur[1]]
    for d in range(4):
        rjumpdis = (abs(cur[0]+jumpDrow[d])+abs(cur[1]+jumpDcol[d]))
        if rjumpdis < rjumpmindis:
            rjumpmindis = rjumpdis
            jumpPos = [cur[0]+jumpDrow[d], cur[1]+jumpDcol[d]]
    jsec += T

    for _ in range(T):
        if newRow > 0:
            newRow -=1
        elif newRow == 0:
            if newCol > 0:
                newCol -=1
            elif newCol == 0:
                break
            else:
                newCol += 1
        else:
            newRow +=1
        
        ssec +=1

    ronestepdis = abs(newRow) + abs(newCol)

    if ronestepdis > rjumpmindis:
        cur = [jumpPos[0],jumpPos[1]]
        cursec = jsec
    else:
        cur = [newRow, newCol]
        cursec = ssec

    if cur[0] == 0 and cur[1] == 0:
        break

print(cursec)