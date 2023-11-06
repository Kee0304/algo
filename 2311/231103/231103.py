import sys
input = sys.stdin.readline

n = int(input().rstrip())

numList = []
numDict = {}
for i in range(n+1):
    numDict[i] = 1

for _ in range(n):
    numList.append(int(input().rstrip()))

def stack():
    cur = 0
    ans = ""

    for i in range(n):
        inputNum = numList[i]
        # 큰 수가 나왔으면 push
        if numDict[inputNum] == 0:
            ans = "NO"
            return ans

        if inputNum > cur:
            # push
            for j in range(cur+1, inputNum+1):
                if numDict[j] == 1:
                    ans += "+\n"
                cur += 1
            # 출력 = pop
            numDict[inputNum] = 0
            cur-=1
            ans += "-\n"
        
        # 작거나 같은 수면 pop
        else:
            cnt = 0
            for j in range(cur, inputNum-1, -1):
                if numDict[j] == 1:
                    cnt += 1
                    numDict[j] = 0
                    ans += "-\n"
                cur -=1

    return ans

print(stack())