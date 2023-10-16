from pprint import pprint
from copy import deepcopy
import sys
input = sys.stdin.readline

R, C, T = map(int,input().split())
drow = [-1,0,1,0]
dcol = [0,1,0,-1]

room = []
dusts = dict()
refreshes = []

for row in range(R):
    inputRow = list(map(int,input().split()))
    for col in range(C):
        if inputRow[col] != 0:
            if inputRow[col] == -1:
                refreshes.append([row, col])
            else:
                dusts[(row,col)]=inputRow[col]
    room.append(inputRow)

upper = refreshes[0]
lower = refreshes[1]

#def move(row, col):
#    # 공기청정기 위쪽
#    if row <= upper-1:
        # 아래로 이동
#        if col == upper[1]:
#            nRow = row+1
            # 공기청정기로 빨려들어감
#            if nRow == upper[0]:


for _ in range(T):
    # 모든 확산은 동시에 일어나므로
    # 1. 먼지가 있는 좌표에 먼지를 깎꼬
    # 2. 확산

    # 먼저 먼지 좌표에 대해 먼지 남기기
    print('먼지 남기기')
    for dust in dusts.keys():
        row = dust[0]
        col = dust[1]
        value = dusts[dust]
        dcnt = 0
        for d in range(4):
            nRow = row+drow[d]
            nCol = col+dcol[d]
            if 0<=nRow<R and 0<=nCol<C:
                if room[nRow][nCol] != -1:
                    dcnt+=1
        room[row][col] -= int(value/5)*dcnt

    copyDict = deepcopy(dusts)
    # 먼지 확산
    for dust in copyDict:
        row = dust[0]
        col = dust[1]
        value = copyDict[dust]
        for d in range(4):
            nRow = row+drow[d]
            nCol = col+dcol[d]
            if 0<=nRow<R and 0<=nCol<C:
                if (nRow,nCol) in dusts:
                    dusts[(nRow,nCol)] += int(value/5)
                else:
                    if room[nRow][nCol] != -1:
                        # 5보다 작은 미세먼지들은 확산이 일어나지 않는다.
                        if int(value/5) > 0:
                            dusts[(nRow,nCol)] = int(value/5)
                if room[nRow][nCol] != -1:
                    room[nRow][nCol] += int(value/5)

    copyDict = deepcopy(dusts)
    for dust in copyDict:
        dusts[dust] = room[dust[0]][dust[1]]

    # 먼지 이동
    copyDict = deepcopy(dusts)


print(dusts)
pprint(room)