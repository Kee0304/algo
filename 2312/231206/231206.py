import sys
input = sys.stdin.readline

N = int(input())


# dp[i][j] = i 자리 수 중 끝이 j인 오르막 수
dp = [[0]*(10) for _ in range(N+1)]

for i in range(1,N+1):
    for j in range(10):
        if i == 1:
            dp[i][j] = 1
        else:
            # 0으로 끝나는 오르막 수는 0....0으로 하나만 존재
            if j == 0:
                dp[i][j] = 1
            # 예를 들어 길이가 i고 끝자리가 9인 오르막 수는
            # 길이가 i-1이고 끝자리가 0~9인 오르막 수에 9를 더한 수이다.
            else:
                dpsum = 0
                for k in range(j+1):
                    dpsum += dp[i-1][k]
                dp[i][j] = dpsum

print(sum(dp[N])%10007)