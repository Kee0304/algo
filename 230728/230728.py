from pprint import pprint
import sys
inp = sys.stdin.readline

def frac(srow,scol, s):
    if s == 0:
        return

    for row in range(srow,srow+N**(s-1)):
        for col in range(scol,scol+N**(s-1)):
            mat[row][col] = 1
            if (s-1) == 0:
                print(row,col)
    

    

# s: 시간, N:시간 1에 N*N 정사각형이 된다
# K: 흰색 정사각형 가운데에 K*K 정사각형
# R1, R2: 행
# C1, C2: 열
# s, N, K, R1, R2, C1, C2 = map(int,inp().split())

s = 3
N = 3
K = 1
R1 = 0
R2 = 8
C1 = 0
C2 = 8

# 전체 정사각형
mat = [[0]*(N**s) for _ in range(N**s)]

frac(N**(s-1),N**(s-1) ,s)