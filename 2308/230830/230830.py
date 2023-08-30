from collections import deque
import sys
inp = sys.stdin.readline

N, M = map(int, inp().split())

mat = []
adjList = [set() for _ in range(N)]
for row in range(N):
    inpList = list(inp().rstrip())
    for col in inpList:
        if inpList[col] == "Y":
            adjList[row].add(col)
            adjList[col].add(row)
    mat.append(inpList)

drow = [-1,0,1,0]
dcol = [0,1,0,-1]
visited = set()
path = []
dq = deque()




            