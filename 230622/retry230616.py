def dessert(startRowIndex, startColIndex):
    global ans
    global N
    # 우측 하단으로 이동할 거리 범위 = 좌측 상단으로 이동할 거리 범위
    for rightDown in range(1, N):
        # 좌측 하단으로 이동할 거리 범위 = 우측 상단으로 이동할 거리 범위
        for leftDown in range(1, N):
            # 좌표가 범위를 벗어나지 않았고 현재 경로 길이가 이전까지 최대 경로길이 보다 길 때
            if ( 
                startRowIndex + rightDown + leftDown <= N-1
                 and startColIndex + rightDown <= N-1
                 and startColIndex - leftDown >= 0
                 and 2*(rightDown+leftDown) > ans
                ):
                # 현재 좌표
                currentRow = startRowIndex
                currentCol = startColIndex

                # 트리거
                canContinue = True

                # 방문 표시
                visited = set()


                # 우측 하단으로 이동 시작
                for _ in range(rightDown):
                    currentRow +=1
                    currentCol +=1
                    # 방문 여부 검사
                    if mat[currentRow][currentCol] not in visited:
                        visited.add(mat[currentRow][currentCol])
                    # 가게가 중복되면 이번 탐색은 실패
                    else:
                        canContinue = False
                        break
                
                # canContinue가 False 이면 continue로 현재 leftDown문을 종료하고 다음으로 넘어간다.
                if canContinue == False:
                    continue

                # 좌측 하단으로 이동 시작
                for _ in range(leftDown):
                    currentRow +=1
                    currentCol -=1
                    # 방문 여부 검사
                    if mat[currentRow][currentCol] not in visited:
                        visited.add(mat[currentRow][currentCol])
                    else:
                        canContinue = False
                        break
                
                if canContinue == False:
                    continue

                # 좌측 상단으로 이동 시작
                for _ in range(rightDown):
                    currentRow -=1
                    currentCol -=1
                    # 방문 여부 검사
                    if mat[currentRow][currentCol] not in visited:
                        visited.add(mat[currentRow][currentCol])
                    else:
                        canContinue = False
                        break
                
                if canContinue == False:
                    continue
                
                
                # 우측 상단으로 이동 시작
                for _ in range(leftDown):
                    currentRow -=1
                    currentCol +=1
                    # 방문 여부 검사
                    if mat[currentRow][currentCol] not in visited:
                        visited.add(mat[currentRow][currentCol])
                    else:
                        canContinue = False
                        break
                
                if canContinue == False:
                    continue
            
                ans = 2*(rightDown+leftDown)

                


T = int(input())

for t in range(1, T+1):
    N = int(input())
    mat = []
    ans = -1

    for _ in range(N):
        mat.append(list(map(int,input().split())))

    # 시작할 수 있는 좌표 제한
    for startRowIndex in range(0,N-1):
        for startColIndex in range(1,N-1):
            dessert(startRowIndex, startColIndex)
    
    print(f'#{t} {ans}')