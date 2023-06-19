def desert():
    return

T = int(input())

for t in range(1, T+1):
    N = int(input())
    mat = []
    visited = [0]*101
    ans = -1

    for _ in range(N):
        mat.append(list(map(int,input().split())))

    for row in range(N-1):
        for col in range(1,N-1):
            desert()
    
