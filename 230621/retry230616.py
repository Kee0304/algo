drow = [1,1,-1,-1]
dcol = [1,-1,-1,1]

T = int(input())

for t in range(1, T+1):
    N = int(input())
    mat = []
    
    ans = -1

    for _ in range(N):
        mat.append(list(map(int,input().split())))

    for startRow in range(2,3):
        for startCol in range(4, 5):
            # visited = set()
            # visited.add(mat[startRow][startCol])
            visited = []
            visited.append(mat[startRow][startCol])
            d = 0
            start = [startRow,startCol]
            row, col = startRow, startCol

            while 1:
                print(visited)
                if d == 0:
                    if row + drow[d]<=N-2 and col + dcol[d]<=N-1:
                        if mat[row + drow[d]][col + dcol[d]] not in visited:
                            #visited.add(mat[row + drow[d]][col + dcol[d]])
                            visited.append(mat[row + drow[d]][col + dcol[d]])
                            row += drow[d]
                            col += dcol[d]
                        
                        else:
                            d = 1
                    
                    else:
                        d = 1

                elif d == 1:
                    if row + drow[d]<=N-1 and 1<=col + dcol[d]:
                        if mat[row + drow[d]][col + dcol[d]] not in visited:
                            #visited.add(mat[row + drow[d]][col + dcol[d]])
                            visited.append(mat[row + drow[d]][col + dcol[d]])
                            row += drow[d]
                            col += dcol[d]
                        else:
                            d = 2
                    
                    else:
                        d = 2


                elif d == 2:
                    if 1<=row + drow[d] and 0<=col + dcol[d]:
                        if mat[row + drow[d]][col + dcol[d]] not in visited:
                            #visited.add(mat[row + drow[d]][col + dcol[d]])
                            visited.append(mat[row + drow[d]][col + dcol[d]])
                            row += drow[d]
                            col += dcol[d]
                        else:
                            d = 3
                    
                    else:
                        d = 3


                elif d == 3:
                    if ((row + drow[d] == startRow) and (col + dcol[d] == startCol)):
                        print(len(visited))
                        if ans < len(visited):
                            ans = len(visited)
                        break
                    
                    if 0<=row + drow[d] and col+dcol[d]<=N-1:
                        if mat[row + drow[d]][col + dcol[d]] not in visited:
                            #visited.add(mat[row + drow[d]][col + dcol[d]])
                            visited.append(mat[row + drow[d]][col + dcol[d]])
                            row += drow[d]
                            col += dcol[d]
                        
                        else:
                            break
                        
                    
                    else:
                        break
                    

    
    print(ans)
    
