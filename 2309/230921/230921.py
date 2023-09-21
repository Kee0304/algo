import sys
input = sys.stdin.readline


def backTrack(lst):
    global ans
    if lst:
        cRow, cCol = lst[-1][0], lst[-1][1]
        if (cRow,cCol) == (9,4):
            print(f'lst = {lst}')
            print(f'cRow, cCol = {cRow, cCol}에서 하나씩 탐색할 거임')
        for nRow in range(cRow, N):
            if nRow == cRow:
                s = cCol+1
            else:
                s = 0
            for nCol in range(s, N):
                # 놓을 수 있는 곳
                if mat[nRow][nCol] != 0:
                    # 여태까지 저장 된 비숍의 위치들
                    for pos in lst:
                        # 대각선 이면 else 실행 안 하게 break
                        if abs(pos[0]-nRow) == abs(pos[1]-nCol):
                            break
                    # 대각선에 걸리지 않았으면 추가하고 다음 단계로
                    else:
                        lst.append((nRow,nCol))
                        visited.add((nRow,nCol))
                        if len(lst) > ans:
                            print(lst)
                            ans = len(lst)
                        backTrack(lst)
                        lst.pop()

drow = [-1,0,1,0]
dcol = [0,1,0,-1]

N = int(input().rstrip())

visitedList = []
mat = []
ans = 0

for row in range(N):
    inpList = list(map(int,input().split()))
    mat.append(inpList)


for row in range(N):
    for col in range(N):
        for vted in visitedList:
            if (row,col) in vted:
                print(f'{(row,col)} in vted')
                break
        else:
            print(f'{row,col}에서 탐색 시작')
            lst = [(row, col)]
            visited = set()
            visited.add((row,col))
            backTrack(lst)
            visitedList.append(visited)

    
print(ans)