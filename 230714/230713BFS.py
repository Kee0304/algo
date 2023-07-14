import collections

drow = [-1, 0, 1, 0]
dcol = [0, 1, 0, -1]

def BFS(dq, culNoR, startRow, startCol):
    global roomnumber
    global thenumberofroom
    for _ in range(len(dq)):
        room = dq.popleft()
        for d in range(4):
            # 범위 체크
            if 0<=room[0]+drow[d]<=N-1 and 0<=room[1]+dcol[d]<=N-1:
                # 인접한 놈이 정확히 1보다 크면
                if mat[room[0]+drow[d]][room[1]+dcol[d]] == mat[room[0]][room[1]]+1:
                    # 덱에 추가
                    dq.append([room[0]+drow[d],room[1]+dcol[d]])
    
    # 덱에 좌표가 있으면
    if len(dq) >=1:
        # BFS 계속
        BFS(dq, culNoR+1, startRow, startCol)

    # 덱이 비었으면 BFS를 끝낸다
    else:
        # BFS 결과 방의 수가 현재 저장된 global 방의 수보다 크면 갱신
        if culNoR > thenumberofroom:
            thenumberofroom = culNoR
            roomnumber = mat[startRow][startCol]
        # 방의 수가 동일하면 방 번호가 작을 때만 갱신
        elif culNoR == thenumberofroom:
            if roomnumber > mat[startRow][startCol]:
                roomnumber = mat[startRow][startCol]
        
        return
    

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
            BFS(collections.deque([[row,col]]),1,row,col)

    print(f'#{t} {roomnumber} {thenumberofroom}')