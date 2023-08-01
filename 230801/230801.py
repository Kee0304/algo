import sys
inp = sys.stdin.readline

def frac(mrow,mcol, s):
    # 프렉탈 도형의 한 변의 길이
    edge = K*(3**(s-1))
    # mrow, mcol을 중점으로 프렉탈 도형을 감싸는 정사각형의 한 변의 길이
    recedge = N*(3**(s-1))
    moveposition = int(recedge/3)

    # 8방향 탐색
    drow = [-moveposition,-moveposition,-moveposition,0,0,+moveposition,+moveposition]
    dcol = [-moveposition,0,+moveposition,-moveposition,+moveposition,-moveposition,0,+moveposition]

    srow = mrow - (edge//2)
    scol = mcol - (edge//2)
    

    for row in range(srow,srow+edge):
        for col in range(scol,scol+edge):
            mat[row][col] = 1
    
    
    # s가 1이면 끝
    if s == 1:
        return
    
    # 다음 프렉탈로
    for d in range(len(drow)):
        frac(mrow+drow[d],mcol+dcol[d], s-1)
    
    

# s: 시간, N:시간 1에 N*N 정사각형이 된다
# K: 흰색 정사각형 가운데에 K*K 정사각형
# R1, R2: 행
# C1, C2: 열
s, N, K, R1, R2, C1, C2 = map(int,inp().split())

# 전체 정사각형
mat = [[0]*(N*(3**(s-1))) for _ in range(N*(3**(s-1)))]

# 중앙에서 시작하자
frac((3**(s-1)*N)//2, (3**(s-1)*N)//2 ,s)

ans = ""

for row in range(R1, R2+1):
    ans += f'{"".join(list(map(str,mat[row][C1:C2+1])))}\n'

print(ans)