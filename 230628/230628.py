# 동서남북으로 이동
drow = [0, 1, 0, -1]
dcol = [1, 0, -1, 0]

# 경로를 만드는 함수
def search(curRow, curCol, step):
    # 만약 6번 이동한 후면
    if step == 7:
        # 경로를 set에 추가
        anset.add(tuple(currentPath))
        return

    # 이동하는 중일 때 동서남북 탐색
    for dIndex in range(4):
        # 이동 가능한 범위 내이면
        if 0<=curRow + drow[dIndex]<=3 and 0<=curCol + dcol[dIndex] <=3:
            # 이동하고
            currentPath.append(mat[curRow + drow[dIndex]][curCol + dcol[dIndex]])
            # 이동한 좌표에서 다시 경로를 탐색하고
            search(curRow + drow[dIndex],curCol + dcol[dIndex], step+1)
            # 경로가 완성되고 돌아왔으면 마지막 이동을 하나 제거하고 다음 이동방향으로 이동
            currentPath.pop()



T = int(input())

for t in range(1, T+1):
    mat = []
    anset = set()
    for _ in range(4):
        mat.append(list(map(int,input().split())))

    # 모든 점을 순회하면서 찾기
    for i in range(4):
        for j in range(4):
            currentPath = [mat[i][j]]
            search(i,j,1)
    
    print(f'#{t} {len(anset)}')