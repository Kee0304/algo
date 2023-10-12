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

print(f'dusts = {dusts}')
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
                dcnt+=1
        print(f'{dust}에 대해 dcnt = {dcnt}')
        dusts[(row,col)] -= int(value/5)*dcnt
        room[row][col] -= int(value/5)*dcnt
        print(f'room[row][col] = {room[row][col]}')
    print('먼지를 깎은 뒤')
    pprint(room)
    extendDusts = []
    copyKeys = list(dusts.keys())[:]
    # 먼지 확산
    print('먼지 확산')
    for dust in copyKeys:
        row = dust[0]
        col = dust[1]
        value = dusts[dust]
        for d in range(4):
            nRow = row+drow[d]
            nCol = row+dcol[d]
            if 0<=nRow<R and 0<=nCol<C:
                if [nRow,nCol] in dust:
                    dusts[(nRow,nCol)] += int(value/5)
                else:
                    dusts[(nRow,nCol)] = int(value/5)
                room[nRow][nCol] += int(value/5)

pprint(room)