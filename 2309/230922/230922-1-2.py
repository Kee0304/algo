import sys
input = sys.stdin.readline

# 대각선 체크
def check(idx):
    cRow, cCol = idx//N, idx%N

    for d in range(4):
        nRow = cRow + diagDrow[d]
        nCol = cCol + diagDcol[d]
        while 0<=nRow<N and 0<=nCol<N:
            if visited[nRow*N+nCol]:
                return False
            nRow += diagDrow[d]
            nCol += diagDcol[d]
    return True

# eo = 짝수 혹은 홀수 판별 파라미너
def diagDFS(idx, eo, cnt):
    if N*N-idx+1+cnt <= ans[eo] or idx >= N*N:
        return

    ans[eo] = max(ans[eo],cnt)
    cRow,cCol = idx//N, idx%N
    j = cCol
    for i in range(cRow, N):
        while j<N:
            v = i*N + j
            if not visited[v] and mat[i][j] == 1 and check(v):
                visited[v] = True
                diagDFS(v, eo, cnt+1)
                visited[v] = False
            # 짝수 홀수 별도이므로 두 칸 이동
            j += 2
        if i%2 == 0:
            j = (eo+1)%2
        else:
            j = eo

# 대각선 탐색
diagDrow = [1,-1,1,-1]
diagDcol = [1,1,-1,-1]


N = int(input().rstrip())
visited=[False]*(N**2)

mat = []

for row in range(N):
    inpList = list(map(int,input().split()))
    mat.append(inpList)

# 대각선 끼리 겹칠 수 있는 부분들을 나눠서 탐색
ans = [0,0]
diagDFS(0,0,0)
diagDFS(1,1,0)

print(sum(ans))

