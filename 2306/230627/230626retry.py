import pprint
from collections import deque

T = int(input())

for t in range(1, T+1):
    # N: 셀의 개수, M: 격리 시간, K: 군집의 개수
    N, M, K = map(int, input().split())
    mat = []
    for _ in range(N):
        mat.append([None]*N)
    biolst = []
    # 이동방향 -> 1:상 2:하 3:좌 4:우
    for _ in range(K):
        row,col,num,dr = map(int,input().split())
        biolst.append([row,col])
        mat[row][col] = deque([[num,dr]])
    
    for i in range (M):
        for bio in biolst:
            # 상
            if mat[bio[0]][bio[1]][0][1] == 1:
                # 일반 셀이면
                if bio[0] >= 2:
                    if mat[bio[0]-1][bio[1]] == None:
                        mat[bio[0]-1][bio[1]] = deque([[mat[bio[0]][bio[1]][0][0],1]])
                    else:
                        mat[bio[0]-1][bio[1]].append([mat[bio[0]][bio[1]][0][0],1])
                # 약품이 칠해진 셀이면
                else:
                    # 반 죽고 방향 반대로
                    if mat[bio[0]-1][bio[1]] == None:
                        mat[bio[0]-1][bio[1]] = deque([[mat[bio[0]][bio[1]][0][0]//2,2]])
                    else:    
                        mat[bio[0]-1][bio[1]].append([mat[bio[0]][bio[1]][0][0]//2,2])
                    
                # 원래 있던 곳 비워주기
                if len(mat[bio[0]][bio[1]]) == 1:
                    mat[bio[0]][bio[1]] = None
                else:
                    mat[bio[0]][bio[1]].popleft()
                    
                # 좌표 수정
                bio[0] -=1

            # 하
            elif mat[bio[0]][bio[1]][0][1] == 2:
                # 일반 셀이면
                if bio[0] <= N-3:
                    if mat[bio[0]+1][bio[1]] == None:
                        mat[bio[0]+1][bio[1]] = deque([[mat[bio[0]][bio[1]][0][0],2]])
                    else:
                        mat[bio[0]+1][bio[1]].append([mat[bio[0]][bio[1]][0][0],2])
                # 약품이 칠해진 셀이면
                else:
                    # 반 죽고 방향 반대로
                    if mat[bio[0]+1][bio[1]] == None:
                        mat[bio[0]+1][bio[1]] = deque([[mat[bio[0]][bio[1]][0][0]//2,1]])
                    else:    
                        mat[bio[0]+1][bio[1]].append([mat[bio[0]][bio[1]][0][0]//2,1])
                    
                # 원래 있던 곳 비워주기
                if len(mat[bio[0]][bio[1]]) == 1:
                    mat[bio[0]][bio[1]] = None
                else:
                    mat[bio[0]][bio[1]].popleft()
                # 좌표 수정
                bio[0] +=1

            # 좌
            elif mat[bio[0]][bio[1]][0][1] == 3:
                # 일반 셀이면
                if bio[1] >= 2:
                    if mat[bio[0]][bio[1]-1] == None:
                        mat[bio[0]][bio[1]-1] = deque([[mat[bio[0]][bio[1]][0][0],3]])
                    else:
                        mat[bio[0]][bio[1]-1].append([mat[bio[0]][bio[1]][0][0],3])
                # 약품이 칠해진 셀이면
                else:
                    # 반 죽고 방향 반대로
                    if mat[bio[0]][bio[1]-1] == None:
                        mat[bio[0]][bio[1]-1] = deque([[mat[bio[0]][bio[1]][0][0]//2,4]])
                    else:    
                        mat[bio[0]][bio[1]-1].append([mat[bio[0]][bio[1]][0][0]//2,4])
                    
                # 원래 있던 곳 비워주기
                if len(mat[bio[0]][bio[1]]) == 1:
                    mat[bio[0]][bio[1]] = None
                else:
                    mat[bio[0]][bio[1]].popleft()
                # 좌표 수정
                bio[1] -=1

            # 우
            else:
                # 일반 셀이면
                if bio[1] <= N-3:
                    if mat[bio[0]][bio[1]+1] == None:
                        mat[bio[0]][bio[1]+1] = deque([[mat[bio[0]][bio[1]][0][0],4]])
                    else:
                        mat[bio[0]][bio[1]+1].append([mat[bio[0]][bio[1]][0][0],4])
                # 약품이 칠해진 셀이면
                else:
                    # 반 죽고 방향 반대로
                    if mat[bio[0]][bio[1]+1] == None:
                        mat[bio[0]][bio[1]+1] = deque([[mat[bio[0]][bio[1]][0][0]//2,3]])
                    else:    
                        mat[bio[0]][bio[1]+1].append([mat[bio[0]][bio[1]][0][0]//2,3])
                
                if len(mat[bio[0]][bio[1]]) == 1:
                    mat[bio[0]][bio[1]] = None
                else:
                    mat[bio[0]][bio[1]].popleft()
                # 좌표 수정
                bio[1] +=1                



        # 미생물이 여러 개 모인 셀을 탐색
        noduple=set()
        for index in range(len(biolst)):
            noduple.add(tuple(biolst[index]))

        for bio in noduple:
            if len(mat[bio[0]][bio[1]]) >=2:
                biosum = 0
                finaldr = mat[bio[0]][bio[1]][0][1]
                maxsize = mat[bio[0]][bio[1]][0][0]
                for index in range(0,len(mat[bio[0]][bio[1]])):
                    biosum += mat[bio[0]][bio[1]][index][0]
                    
                    if mat[bio[0]][bio[1]][index][0] > maxsize:
                        finaldr = mat[bio[0]][bio[1]][index][1]
                        maxsize = mat[bio[0]][bio[1]][index][0]

                
                mat[bio[0]][bio[1]] = deque([[biosum,finaldr]])
            
            else:
                mat[bio[0]][bio[1]] = deque([mat[bio[0]][bio[1]][0]])
        
        biolst = list(map(list, list(noduple)))

    res = 0
    for bio in biolst:
        res += mat[bio[0]][bio[1]][0][0]
    
    print(f'#{t} {res}')
