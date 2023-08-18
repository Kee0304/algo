import sys
inp = sys.stdin.readline

inpStr = inp().rstrip()
length = len(inpStr)
# dp[left][right] : left~right 까지의 부분 문자열을 팰린드롬으로 만들기 위한 최소의 연산 수
# left는 왼쪽 끝부터 오른쪽으로 이동, right는 오른쪽 끝부터 왼쪽으로 이동
dp = [[-1]*length for _ in range(length)]

# 왼쪽에 하나를 삽입하거나 오른쪽에서 하나를 삭제한 경우
# 예를 들어 부분문자열 czxcb에서 bczxcb를 만들거나 czxc를 만든 경우
# czxcb를 확인해야 했던 것이 czxc만 확인하면 된다. 즉 left는 그대로, right는 하나 줄어든다.
# dp[left][right] = dp[left][right-1] + 1

# 오른쪽에 하나를 삽입하거나 왼쪽에서 하나를 삭제한 경우
# 예를 들어 부분문자열 axbzc에서 xbzc를 만들거나 axbzca를 만든 경우
# axbzc를 확인해야 했던 것이 xbzc만 확인하면 된다. 즉 left가 하나 늘었고 right는 그대로이다.
# dp[left][right] = dp[left+1][right] + 1

# 하나의 문자열을 교환한 경우
# 예를 들어 hfhwuyg에서 맨 왼쪽의 h를 g로, 혹은 맨 오른쪽의 g를 h로 바꾸었으면
# hfhwuyg를 확인해야 했던 것이 fhwuy만 확인하면 된다. left+1, right-1
# 단 이 경우 현재 left와 right가 같다면 연산을 해줄 필요 자체가 없다.
# dp[left][right] = dp[left+1][right-1] + (inpStr[left]!=intStr[right])

def pelin(left, right, string):
    if dp[left][right] != -1:
        return dp[left][right]
    
    if left >= right:
        return 0

    dp[left][right] = min(
        pelin(left+1,right,string)+1, 
        pelin(left,right-1,string)+1, 
        pelin(left+1,right-1,string)+(string[left]!=string[right])
        )
    
    return dp[left][right]

ans = pelin(0, length-1, inpStr)

# 임의의 두 문자열을 교체
for i in range(length):
    for j in range(i+1, length):
        if inpStr[i] == inpStr[j]:
            pass
        else:
            # 문자열을 교체하고 다시 dp 연산
            dp = [[-1]*length for _ in range(length)]
            strList = list(inpStr)
            strList[i], strList[j] = strList[j], strList[i]
            changedStr = "".join(strList)
            # 교환을 한 시점에서 연산 횟수+1
            ans = min(ans, pelin(0, length-1, changedStr)+1)


print(ans)