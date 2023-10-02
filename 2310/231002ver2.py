import sys
input = sys.stdin.readline

K, N= map(int,input().split())

lineList = [0]*K

for i in range(K):
    lineList[i] = int(input())

maxLen = max(lineList)

ans = 0

start = 1
end = maxLen

while start <= end:
    mid = (start+end)//2
    cnt = 0
    for i in range(K):
        cnt += lineList[i]//mid
    
    if start == end:
        if cnt >= N:
            if mid > ans:
                ans = mid
        break
    
    else:
        if cnt >= N:
            if mid > ans:
                ans = mid
            if mid +1 <= end:
                start = mid+1
        
        else:
            end = mid

print(ans)