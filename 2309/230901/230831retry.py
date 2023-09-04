from collections import deque
import sys

inp = sys.stdin.readline

drow = [-1,0,1,0]
dcol = [0,1,0,-1]

N, M = map(int, inp().split())

mat = []

red = None
blue = None
goal = None

for row in range(N):
    inpList = list(inp().rstrip())

    for col in range(M):
        if inpList[col] == "R":
            red = (row, col)
        elif inpList[col] == "B":
            blue = (row, col)
        elif inpList[col] == "O":
            goal = (row, col)
    
    mat.append(inpList)

dq=deque([[red,blue,0]])
visited = set()
visited.add((red, blue))

def goStraight(direction, curPos):
    length = 0
    pos = list(curPos)
    # 구슬 이동
    while (
        1<= pos[0]+drow[direction] <= N-2 and
        1<= pos[1]+dcol[direction] <= M-2 and
        mat[pos[0]+drow[direction]][pos[1]+dcol[direction]] != "#"
        ):
        pos[0] += drow[direction]
        pos[1] += dcol[direction]
        length+=1
        
        if (pos[0],pos[1]) == goal:
            return ("Hole")
    return (pos[0], pos[1], length)

cntList = []
def bfs():
    global ans
    
    while dq:
        curPoses = dq.popleft()
        curRed = curPoses[0]
        curBlue = curPoses[1]
        cnt = curPoses[2]
        if cnt >= 10:
            break

        # 기울이기
        for d in range(4):
            nextRed = goStraight(d,curRed)
            nextBlue = goStraight(d,curBlue)
            # 기울여서 파란 공이 구멍에 떨어지면 안 된다
            if nextBlue != "Hole":
                if nextRed == "Hole":
                    cntList.append(cnt+1)
                    break

                else:
                    if nextRed[0] == nextBlue[0] and nextRed[1] == nextBlue[1]:
                        if nextRed[2] > nextBlue[2]:
                            nextRed = (nextRed[0]-drow[d], nextRed[1]-dcol[d], nextRed[2])
                        else:
                            nextBlue = (nextBlue[0]-drow[d], nextBlue[1]-dcol[d], nextBlue[2])

                    if ((nextRed[0],nextRed[1]), (nextBlue[0],nextBlue[1])) not in visited:
                        visited.add(((nextRed[0],nextRed[1]), (nextBlue[0],nextBlue[1])))
                        dq.append(((nextRed[0],nextRed[1]),(nextBlue[0],nextBlue[1]),cnt+1))
    
    else:
        return
bfs()
if len(cntList) >=1:
    print(min(cntList))
else:
    print(-1)
