from collections import deque
import sys
inp = sys.stdin.readline

drow = [-1, 0, 1, 0]
dcol = [0, 1, 0, -1]

mat = []
alone = set()
for _ in range(5):
    mat.append(list(inp().rstrip()))

pieces = []
visited = set()
for row in range(5):
    for col in range(5):
        piece = []
        if mat[row][col] == "*":
            if ((row,col)) not in visited:
                piece.append((row,col))
                dq = deque()
                dq.append((row,col))
                visited.add((row,col))
                while dq:
                    cur = dq.popleft()
                    curRow = cur[0]
                    curCol = cur[1]
                    for d in range(4):
                        nextRow = curRow+drow[d]
                        nextCol = curCol+dcol[d]
                        if 0<= nextRow <=4 and 0<= nextCol <=4:
                            if mat[nextRow][nextCol] == "*":
                                if (nextRow,nextCol) not in visited:
                                    piece.append((nextRow,nextCol))
                                    dq.append((nextRow,nextCol))
                                    visited.add((nextRow,nextCol))
                
        if len(piece) >=1:
            pieces.append(piece)

ans = 0



def combine(pieces):
    global ans
    mindist = 100
    minRowMove = 50
    minColMove = 50
    mindistOther = None
    for piece in pieces:
        for otherpiece in pieces:
            if piece != otherpiece:
                for startPos in piece:
                    for endPos in otherpiece:
                        rowMove = endPos[0]-startPos[0]
                        colMove = endPos[1]-startPos[1]
                        dist = abs(rowMove)+abs(colMove)
                        if dist < mindist:
                            mindist = dist
                            minRowMove = rowMove
                            minColMove = colMove
                            mindistOther = otherpiece
        
        
        if minRowMove == 0:
            if minColMove >= 1:
                minColMove -=1
            elif minColMove <= -1:
                minColMove +=1
        
        elif minColMove == 0:
            if minRowMove >= 1:
                minRowMove -=1
            elif minRowMove <= -1:
                minRowMove +=1

        else:
            if abs(minRowMove) >= abs(minColMove):
                if minRowMove >= 1:
                    minRowMove -=1
                elif minRowMove <= -1:
                    minRowMove +=1
            
            else:
                if minColMove >= 1:
                    minColMove -=1
                elif minColMove <= -1:
                    minColMove +=1

        for pos in piece:
            mindistOther.append((pos[0]+minRowMove, pos[1]+minColMove))
        ans += abs(minRowMove)+abs(minColMove)
        pieces.remove(piece)
        return

while len(pieces) >= 2:
    print(pieces)
    pieces.sort(key=lambda p: len(p))
    combine(pieces)
    
print(ans)