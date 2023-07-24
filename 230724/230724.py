from collections import deque
import sys
inp = sys.stdin.readline


for _ in range(int(inp())):
    N, K = map(int,inp().split())
    buildTime = [0]+list(map(int,inp().split()))
    acBuildTime = [None]*(N+1)
    # 건물 번호를 인덱스로 하여 도달할 수 있는 건물을 집어넣을 리스트
    adjlst = [[] for _ in range(N+1)]
    # 탐색이 필요한 선행 건물 남은 개수를 위한 리스트
    linked = [0] + [0]*N
    
    for _ in range(K):
        st, en = map(int,inp().split())
        adjlst[st].append(en)
        linked[en] += 1
    
    W = int(inp())

    dq = deque()

    # 선행 건물이 없는 건물들을 시작 건물들로 설정
    for i in range(1, N+1):
        if linked[i] == 0:
            dq.append(i)
            # 선행 건물이 없으므로 건설 시간 = 누적 시간 설정
            acBuildTime[i] = buildTime[i]
    
    # 덱이 빌 때까지
    while dq:
        cur = dq.popleft()
        for en in adjlst[cur]:
            # 선행 건물 하나 탐색
            linked[en] -= 1

            # 여태까지 누적 시간과 이번 누적 시간 비교
            if acBuildTime[en] == None:
                acBuildTime[en] = buildTime[en] + acBuildTime[cur]
            else:
                acBuildTime[en] = max(acBuildTime[en], buildTime[en] + acBuildTime[cur])
            
            # 선행 건물들을 다 탐색한 = 누적 시간이 확정된 건물을 덱에 추가
            if linked[en] == 0:
                dq.append(en)
            
        
        # 승리 건물의 선행 건물을 다 탐색했음 = 끝
        if linked[W] == 0:
            break

    print(acBuildTime[W])