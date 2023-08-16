import sys
inp = sys.stdin.readline

# 행, 열의 개수
N, M = map(int,inp().split())
table = []
colList = [0]*M
# 첫 상태
for _ in range(N):
    inpList = list(map(int,"".join(inp().split())))
    table.append(inpList)

K = int(inp())
ans = 0

for rowIndex in range(N):
    row = table[rowIndex]
    zero = row.count(0)
    # 켜질 수 있는 행인지 확인
    # 꺼져있는 열보다 스위치 누르는 횟수가 크면 다 못 켠다.
    # 일단 다 킨 상태로 만들 수 있을 때, 두 번 누르면 다시 원래상태로 돌릴 수 있으므로
    # K가 짝수이면 0이 짝수개, K가 홀수이면 0이 홀수 개일 때 행을 다 켤 수 있다.
    if zero <= K and zero%2 == K%2:
        # 켜질 수 있는 행이면 같은 놈들을 찾는다.
        cnt = 0
        for subRowIndex in range(N):
            if table[rowIndex] == table[subRowIndex]:
                cnt +=1
        
        if cnt > ans:
            ans = cnt

print(ans)


