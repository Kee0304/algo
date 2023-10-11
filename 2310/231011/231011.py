from pprint import pprint
import sys
input = sys.stdin.readline

R, C, T = map(int,input().split())

drow = [-1,0,1,0]
dcol = [0,1,0,-1]

room = []
dusts = []
refreshes = []

for row in range(R):
    inputRow = list(map(int,input().split()))
    for col in range(C):
        if inputRow[col] != 0:
            if inputRow[col] != -1:
                refreshes.append([row, col])
            else:
                dusts.append([row,col])
    room.append(inputRow)

print(f'dusts = {dusts}')
for _ in range(T):
    # 미세먼지들에 대해
    print('미세먼지 확산')
    lenPos = len(dusts)
    for i in range(lenPos):
        cRow = dusts[i][0]
        cCol = dusts[i][1]
        # 확산 방향 수
        dcnt = 0
        # 가능한 확산 좌표
        able = []
        for d in range(4):
            nRow = cRow + drow[d]
            nCol = cCol + dcol[d]
            # 범위 내이고 공기청정기가 없는 곳
            if 0<=nRow<R and 0<=nCol<C:
                if room[nRow][nCol] != -1:
                    dcnt+=1
                    # 미세먼지 좌표에도 더해줌
                    dusts.append([nRow,nCol])
                    able.append([nRow,nCol])
        
        room[cRow][cCol] -= int(room[cRow][cCol]/5)*dcnt
        for (nRow, nCol) in able:
            room[nRow][nCol] += int(room[cRow][cCol]/5)

    # 공기청정기 위쪽, 아래쪽
    for i in range(2):
        rRow = refreshes[i][0]
        rCol = refreshes[i][1]
        if i == 0:
            print('위쪽')
            # 위로 올라갈 미세먼지
            toUp = room[rRow][-1]
            # 오른쪽으로 한 칸씩 땡김
            for loopCol in range(C-1,0,-1):
                room[rRow][loopCol] = room[rRow][loopCol-1]
            # 미세먼지 옆에 0 추가
            room[rRow][1] = 0
            
            # 왼쪽으로 이동할 미세먼지
            toLeft = room[0][C-1]
            # 위쪽으로 한 칸씩 땡김
            for loopRow in range(2,rRow-1):
                room[loopRow-1][C-1] = room[loopRow][C-1]
            # 올라온 미세먼지
            room[rRow-1][C-1] = toUp

            # 아래로 이동할 미세먼지
            toDown = room[0][0]
            # 왼쪽으로 한 칸씩 땡김
            for loopCol in range(0, C-2):
                room[0][loopCol] = room[0][loopCol+1]
            # 왼쪽으로 온 미세먼지
            room[0][C-2] = toLeft


            for loopRow in range(rRow-1, 0, -1):
                room[loopRow][0] = room[loopRow-1][0]
            room[0][1] = toDown

            rem = None
            for dust in dusts:
                if dust[0] == rRow and dust[1]<=C-2:
                    dust[1]+=1
                elif 0<=dust[0]<=rRow and dust[1] == C-1:
                    dust[0]-=1
                elif dust[0]==0 and 1<=dust[1]:
                    dust[1]-=1
                elif 0<=dust[0]<rRow and dust[1] == 0:
                    dust[0]+=1
                elif dust[0] == rRow-1 and dust[1] == 0:
                    rem = [dust[0],dust[1]]
            
            try:
                dust.remove(rem)
            except:
                pass

        if i == 1:
            print('아래쪽')
            # 위로 올라갈 미세먼지
            toDown = room[rRow][-1]
            # 오른쪽으로 한 칸씩 땡김
            for loopCol in range(C-1,0,-1):
                room[rRow][loopCol] = room[rRow][loopCol-1]
            # 미세먼지 옆에 0 추가
            room[rRow][1] = 0

            toLeft = room[R-1][C-1]
            for loopRow in range(R-1, rRow, -1):
                room[loopRow][C-1] = room[loopRow-1][C-1]
            room[rRow+1][C-1] = toDown

            toUp = room[R-1][0]
            for loopCol in range(0,C-1):
                room[0][loopCol] = room[0][loopCol+1]
            room[R-2][C-1] = toLeft

            for loopRow in range(rRow+1, R-1):
                room[loopRow][0] = room[loopRow+1][0]
            room[R-2][0]=toUp

            rem = None
            for dust in dusts:
                if dust[0] == rRow and dust[1]<=C-2:
                    dust[1]+=1
                elif rRow<=dust[0]<=R-1 and dust[1] == C-1:
                    dust[0]+=1
                elif dust[0]==R-1 and 1<=dust[1]:
                    dust[1]-=1
                elif rRow+1<=dust[0]<=R-1 and dust[1] == 0:
                    dust[0]-=1
                elif dust[0] == rRow+1 and dust[1] == 0:
                    rem = [dust[0],dust[1]]
            
            try:
                dust.remove(rem)
            except:
                pass

    
pprint(room)
 


        

