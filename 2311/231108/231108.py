import sys
input = sys.stdin.readline

first_Str = list(input().rstrip())
second_Str = list(input().rstrip())
fLen = len(first_Str)
sLen = len(second_Str)


dp = [[0]*(sLen+1) for _ in range(fLen+1)]


# ACAYKP
# CAPCAK
# 순회 편의를 위해 i는 i-1번째 문자열, j 는 j-1번째 문자열로 설정
# first_Str[0], first[1] = 1 이면 A로 같다
# 일단 dp[1][2] = 1이 된다.

# i = 2, j = 4 이면 first_Str[1]은 C, second_Str[3]은 C로 같다
# 그렇다면 LCS의 길이 dp[2][4]는 여태까지의 LCS 길이에 1을 더해야 하는데
# 이는 dp[1][3] 까지 순회했을 때 가장 긴 LCS 길에이 1을 더한 것이다.

# i = 5, j = 5 이면 first_Str[4]는 K, second_Str[4]는 C로 다르다
# 그렇다면 first_Str[3]=Y, second_Str[4]=A까지 구한 LCS = dp[4][5] = 3(ACA 가능)와
# fisrt_Str[4]=K, second_Str[3]=C까지 구한 LCS = dp[5][4] = 2(AC, CA가능) 중 큰 놈을 고르면 된다
# 그렇다면 dp[5][5] = 3 


# 첫번째 문자열 순회, i 는 first_Str의 i-1번째 문자를 가리킨다.
for i in range(1,fLen+1):
    # 두번째 문자열 순회, j는 second_Str의 j-1 번째 문자열을 가리킨다.
    for j in range(1,sLen+1):
        # 만약 문자가 같다면
        if first_Str[i-1] == second_Str[j-1]:
            # i-1, j-1 까지의 LCS 길이에 1을 더해준다.
            dp[i][j] = dp[i-1][j-1] + 1
        # 문자가 다르면
        else:
            # i, j-1 까지의 LCS 길이와 i-1, j 까지의 LCS 길이 중 긴 것을 선택
            dp[i][j] = max(dp[i][j-1], dp[i-1][j])

print(dp[fLen][sLen])