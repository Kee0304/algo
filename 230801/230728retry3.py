# 저번 풀이의 경우 프렉탈을 모두 완성하고 그 중에서 출력하는 방식이었다
# 그런데 전체 평면의 범위가 8**10 으로 터무니 없이 큰 것을 발견했다.
# 즉, 모든 평면을 만들지 말고 필요한 부분만 그때그때 출력할 필요가 있다
# 주어진 범위를 돌면서 해당 좌표가 칠해지는 부분인지 아닌지 판별해야 한다

import sys
inp = sys.stdin.readline

# s, N, K, R1, R2, C1, C2 = map(int,inp().split())
s = 3
N = 4
K = 2
R1 = 0
R2 = N**s
C1 = 0
C2 = N**s
ans = ""

# 현재 프렉탈 평면을 감싸는 정사각형의 크기
recedge = N**s

def frac(row,col, recedge):
    # 만약 정사각형의 크기가 1이 될 때까지 왔으면 못 칠하는 좌표다
    if recedge == 1:
        return "0"
    
    # 탐색할 평면 크기를 줄이자
    # N**(s) 에서 s가 1씩 줄어듬
    srecedge = recedge // N

    # 지금 정사각형 크기에 대해, 만약 칠해야 하는 좌표면 칠한다
    if (
        (srecedge*(N-K)//2 <= row < srecedge*(N+K)//2)
        and (srecedge*(N-K)//2 <= col < srecedge*(N+K)//2)
        ):
        return "1"
    
    # recedge에 대해서 아직 칠하지 않았으므로 그 아랫단계 정사각형에 대해서도 판별하러 가자
    return frac(row%srecedge, col%srecedge, srecedge)

for row in range(R1, R2+1):
    for col in range(C1, C2+1):
        ans+=frac(row,col,recedge)
    ans += '\n'

print(ans)