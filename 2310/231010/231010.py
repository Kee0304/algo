#from pprint import pprint
import sys
input = sys.stdin.readline

N, K = map(int,input().split())

thingList = [[0,0]]

for _ in range(N):
    thingList.append(list(map(int,input().split())))

# dp[n][k] = n번째 물건까지 탐색했을 때 무게가 k인 가방의 최대 가치
dp = [[0]*(K+1) for _ in range(N+1)]


# 물건에 대해
for i in range(1,N+1):
    # 무게를 순회한다
    for j in range(1, K+1):
        weight = thingList[i][0]
        value = thingList[i][1]
        # 만약 순회하는 무게의 인덱스 j가 현재 물건의 무게보다 작으면
        if j < weight:
            # j에 대한 최대 가치는 그 전 인덱스와 같다
            dp[i][j] = dp[i-1][j]
        # 만약 j가 현재 물건 i의 무게보다 무겁다면
        else:
            # 그 전 인덱스와 물건 i를 추가했을 때의 가치를 비교해서 넣는다.
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-weight]+value)

# 2,3 5,3이 연속되어있는 물품이 있는 리스트에 대해
# 예를 들어 5,3 인 물건에 대해 무게가 8일 때 최대 가치를 구할 때
# 그 무게는 2,3 인 물건에 대해 무게가 8일 때 최대 가치 dp[i-1][j]와
# 2,3인 물건에 대해 무게가 j-weight(현재 물건 5의 무게)에 대한 가치에 value(현재 물건 가치 3)을 더한 놈 중 최대를 선택 

#pprint(dp)
print(dp[N][K])