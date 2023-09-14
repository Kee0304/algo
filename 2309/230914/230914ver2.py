from bisect import insort
import sys
inp = sys.stdin.readline

N = int(inp().rstrip())
lst = []

for _ in range(N):
    lst.append(int(inp()))

ansList = list(map(str, sorted(lst)))
ans = "\n".join(ansList)
print(ans)