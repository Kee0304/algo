import collections

drow = [-1, 0, 1, 0]
dcol = [0, 1, 0, -1]

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
            dq = collections.deque([[row,col]])
            curNoR = 0
            while len(dq) >=1:
                curNoR +=1
                for _ in range(len(dq)):
                    room = dq.popleft()
                    for d in range(4):
                    # 범위 체크
                        if 0<=room[0]+drow[d]<=N-1 and 0<=room[1]+dcol[d]<=N-1:
                            # 인접한 놈이 정확히 1보다 크면
                            if mat[room[0]+drow[d]][room[1]+dcol[d]] == mat[room[0]][room[1]]+1:
                                # 덱에 추가
                                dq.append([room[0]+drow[d],room[1]+dcol[d]])

            if curNoR > thenumberofroom:
                thenumberofroom = curNoR
                roomnumber = mat[row][col]
            elif curNoR == thenumberofroom:
                if roomnumber > mat[row][col]:
                    roomnumber = mat[row][col]

    
    print(f'#{t} {roomnumber} {thenumberofroom}')