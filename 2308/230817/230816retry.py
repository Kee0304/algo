from collections import deque
from itertools import combinations, permutations
import sys
inp = sys.stdin.readline

drow = [-1, 0, 1, 0]
dcol = [0, 1, 0, -1]

def pieces(points):
    visited = set()
    visited.add(points[0])
    dq = deque()
    dq.append(points[0])
    size = 1
    curmat = [["."]*5 for _ in range(5)]
    
    for row,col in points:
        curmat[row][col] = "*"

    while dq:
        curRow, curCol = dq.popleft()
        for d in range(4):
            nextRow = curRow + drow[d]
            nextCol = curCol + dcol[d]
            if 0<= nextRow <=4 and 0<= nextCol <=4:
                if (nextRow,nextCol) not in visited:
                    if curmat[nextRow][nextCol] == "*":
                        visited.add((nextRow,nextCol))
                        dq.append((nextRow,nextCol))
                        size +=1
    
    if size == len(points):
        return True
    else:
        return False
    
def dist(a,b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])

mat = []

for _ in range(5):
    mat.append(list(inp().rstrip()))

points = []
for row in range(5):
    for col in range(5):
        if mat[row][col] == "*":
            points.append((row,col))
pointsNum = len(points)
combs=list(combinations([i for i in range(25)], pointsNum))
ans = 51
for comb in combs:
    curPoints = []
    for i in comb:
        row = i//5
        col = i%5
        curPoints.append((row, col))
    
    if not pieces(curPoints):
        continue

    permu = list(permutations([i for i in range(pointsNum)],pointsNum))
    for perm in permu:
        temp = 0
        for i in range(pointsNum):
            temp+=dist(points[i],curPoints[perm[i]])
        if temp < ans:
            ans = temp

print(ans)
