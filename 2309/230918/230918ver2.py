import sys
inp = sys.stdin.readline

N = int(inp().rstrip())

inpList = []

for _ in range(N):
    inpList.append(list(map(int,inp().split())))

sortedList = sorted(inpList, key = lambda x: (x[0], x[1]))

ans = "\n".join([f"{key} {val}" for key, val in sortedList])
print(ans)