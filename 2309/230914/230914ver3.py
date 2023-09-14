import sys
inp = sys.stdin.readline

def forceSort(num):
    while 1:
        mid = start+end//2
        if dq[mid-1] <= num <= dq[mid]:
            dq.insert(mid, num)
            break
        elif num<dq[mid-1]:
            end = mid-1
        elif dq[mid]<num:
            start == mid
        


N = int(inp().rstrip())
lst = []

for _ in range(N):
    lst.append(int(inp()))

ansList = list(map(str, lst))
ans = "\n".join(ansList)
print(ans)
