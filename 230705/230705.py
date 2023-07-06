# n = 현재 행
def nQueen(n):
    global ans

    # 모든 행에 조건에 맞춰 queen을 놓는 데에 성공했으면
    if n == N:
        ans+=1
        return

    # 하나씩 넣어본다
    for i in range(N):
        # n행 i열에 queen을 넣어보자
        col[n] = i
        
        # n에 i를 놓을 수 있으면 다음 단계로 넘어간다 
        if isPossible(n) == True:
            nQueen(n+1)


# 놓을 수 있는 자리인지 아니인지 판별하는 함수
def isPossible(curRow):
    # 이전 행들의 queen들을 돌아보면서
    for forRow in range(curRow):
        if (
            # 같은 열에 위치하거나
            col[forRow] == col[curRow]
            or
            # 대각선 상에 있으면
            abs(col[forRow] - col[curRow]) == abs(forRow-curRow)  
        ):
            # 놓을 수 없다
            return False
        
    # 다 탐색 했는데 놓을 수 있다.
    return True



T = int(input())

for t in range(1, T+1):
    N = int(input())
    col = [-1]*N
    
    ans = 0

    nQueen(0)

    print(f'#{t} {ans}')