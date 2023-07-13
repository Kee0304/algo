drow = [-1, 0, 1, 0]
dcol = [0, 1, 0, -1]

def DFS(row, col, currentnumberofroom,startRow,startCol):
    global roomnumber
    global thenumberofroom
    # DFS
    for d in range(4):
        # 범위 체크
        if 0<=row+drow[d]<=N-1 and 0<=col+dcol[d]<=N-1:
            # 인접한 놈이 정확히 1보다 크면
            if mat[row+drow[d]][col+dcol[d]] == mat[row][col]+1:
                # 방 개수 갱신
                if currentnumberofroom+1 >= thenumberofroom:
                    thenumberofroom = currentnumberofroom+1
                    # 번호 작은 놈으로 갱신
                    if roomnumber > mat[startRow][startCol]:
                        roomnumber = mat[startRow][startCol]
            
                DFS(row+drow[d],col+dcol[d], currentnumberofroom+1,startRow,startCol)

T = int(input())

for t in range(1,T+1):
    N = int(input())
    mat = []

    for _ in range(N):
        mat.append(list(map(int,input().split())))

    roomnumber = N**2
    thenumberofroom = 1

    for row in range(N):
        for col in range(N):
            DFS(row,col,1,row,col)

    
    print(f'#{t} {roomnumber} {thenumberofroom}')