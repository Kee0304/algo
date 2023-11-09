import sys
input = sys.stdin.readline
#f = open("175.txt", "r")
#n = int(f.readline())
#intList = list(map(int,f.readline().split()))


n = int(input())
intList = list(map(int,input().split()))
partSum=[]
part = 0

# N
for i in range(n):
    if intList[i] < 0:
        if part <= 0:
            part+=intList[i]
        else:
            partSum.append(part)
            part = 0
            part += intList[i]

    else:
        if part >= 0:
            part += intList[i]
        else:
            partSum.append(part)
            part = 0
            part += intList[i]

else:
    if part != 0:
        partSum.append(part)


maxIndexes = []
curMax = max(intList)
partLen = len(partSum)

ans = 0

# 길이가 1 -> 증가만 하거나 감소만한다.
if len(partSum) == 1:
    for i in range(partLen):
        # +만 있으면 다 더해주면 끝
        if intList[i] > 0:
            ans = sum(intList)
        
        # -만 있으면 가장 큰 수로 끝
        else:
            ans = max(intList)


# N
else:
    for i in range(partLen):
        if partSum[i] == curMax:
            maxIndexes.append(i)
        elif partSum[i] > curMax:
            maxIndexes = [i]
            curMax = partSum[i]
    maxSum = partSum[maxIndexes[0]]
    ans = maxSum
    # N
    for i in range(len(maxIndexes)):
        curIndex = maxIndexes[i]
        dp = [0]*partLen
        dp[curIndex] = maxSum
        
        # N
        for i in range(curIndex-1,-1,-1):
            dp[i] = partSum[i]+dp[i+1]
            if dp[i] > ans:
                ans = dp[i]

        for i in range(curIndex+1,partLen):
            dp[i] = partSum[i]+dp[i-1]
            if dp[i] > ans:
                ans = dp[i]

# N^2
print(max(dp))