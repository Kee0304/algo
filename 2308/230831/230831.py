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
        
        if (pos[0],pos[1]) == goal:
            return ("Hole")

    return (pos[0], pos[1], length)

ans = 0

def bfs():
    global ans
    
    while dq:
        curPoses = dq.popleft()
        curRed = curPoses[0]
        curBlue = curPoses[1]
        cnt = curPoses[2]
        print(f'현재 {curRed, curBlue, cnt} 탐색 중')
        if cnt >= 11:
            ans = -1
            return

        # 기울이기
        for d in range(4):
            nextRed = goStraight(d,curRed)
            nextBlue = goStraight(d,curBlue)
            print(f'{d}방향으로 굴러간 결과 {nextRed, nextBlue}')
            # 기울여서 파란 공이 구멍에 떨어지면 안 된다
            if nextBlue[0] != "Hole":
                if nextRed[0] == "Hole":
                    return cnt +1

                else:
                    if nextRed == nextBlue:
                        if nextRed[2] > nextBlue[2]:
                            nextRed = (nextRed[0]+drow[d], nextRed[1]+dcol[d], nextRed[2])
                        else:
                            nextBlue = (nextBlue[0]+drow[d], nextBlue[1]+dcol[d], nextBlue[2])

                    if ((nextRed[0],nextRed[1]), (nextBlue[0],nextBlue[1])) not in visited:
                        visited.add(((nextRed[0],nextRed[1]), (nextBlue[0],nextBlue[1])))
                        dq.append(((nextRed[0],nextRed[1]),(nextBlue[0],nextBlue[1]),cnt+1))
    
    else:
        ans = -1
        return
bfs()
print(ans)