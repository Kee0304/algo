from pprint import pprint
import sys
inp = sys.stdin.readline

# 다음 8방향 탐색


# 한 변의 길이 = k***3(s-1)
# 예를 들어 N=5, K=3일 때 s=2에서 한 변의 길이는 K*(3**(s-1)) = 9
# N=4, K=2 s=2면 한 변의 길이는 K*(3**(s-1)) = 6
# N=5, K=3 s=3: K*(3**(s-1)) = 27
# 시작 지점의 경우 한 변의 길이에 대해 변한다

def frac(srow,scol, s):

    edge = K*(3**(s-1))
    if edge == 0:
        edge = 1

    for row in range(srow,srow+edge):
        for col in range(scol,scol+edge):
            print(f'row,col = {row,col}')
            mat[row][col] = 1
    
    if s == 1:
        return

    for d in range(8):
        frac(srow+int(drow[d]*edge),scol+int(dcol[d]*edge), s-1)
    

    

# s: 시간, N:시간 1에 N*N 정사각형이 된다
# K: 흰색 정사각형 가운데에 K*K 정사각형
# R1, R2: 행
# C1, C2: 열
# s, N, K, R1, R2, C1, C2 = map(int,inp().split())

s = 2
N = 5
K = 1
R1 = 0
R2 = 8
C1 = 0
C2 = 8

# 전체 정사각형
mat = [[0]*(N*(3**(s-1))) for _ in range(N*(3**(s-1)))]

drow = [-(2/(3*K)),-(2/(3*K)),-(2/(3*K)),+(K/(3*K)),+(K/(3*K)),+((2+2*K)/(3*K)),+((2+2*K)/(3*K)),+((2+2*K)/(3*K))]
dcol = [-(2/(3*K)),+(K/(3*K)),+((2+2*K)/(3*K)),-(2/(3*K)),+((2+2*K)/(3*K)),-(2/(3*K)),+(K/(3*K)),+((2+2*K)/(3*K))]

# 전체 정사각형의 한 변의 길이 = (3**(s-1))*N
# 예를 들어 N = 4, K = 2, s = 3 : 36
# 예를 들어 N = 5, K = 1, s = 3 : 45

# 시작 좌표의 위치: 전체 사각형의 길이 - 한 변의 길이 / 2
frac(int((((3**(s-1))*N)-((3**(s-1))*K))/2),int((((3**(s-1))*N)-((3**(s-1))*K))/2) ,s)

pprint(mat, width= 200)