import sys
inp = sys.stdin.readline

N = int(inp().rstrip())

inpDict = dict()
for _ in range(N):
    key, val = map(int,inp().split())
    if key in inpDict :
        inpDict[key].append(val)
    else:
        inpDict[key] = [val]

sortedKeyList = sorted(list(dict.keys(inpDict)))
ans = ""
for key in sortedKeyList:
    valList = sorted(inpDict[key])
    for val in valList:
        ans += f'{key} {val}\n'

print(ans)