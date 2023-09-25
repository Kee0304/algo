import sys
input = sys.stdin.readline

strList = list(input().rstrip())
strLen = len(strList)
ans = strLen

for i in range(strLen):
    if strList[i] == "=":
        try:
            if strList[i-1] == "c" or strList[i-1] == "s":
                ans -=1
        except:
            continue

        
        try:
            if strList[i-1] == "z":
                try:
                    if strList[i-2] == "d":
                        ans -=2
                    else:
                        ans -=1
                except:
                    continue
        except:
            continue
    
    elif strList[i] == "-":
        try:
            if strList[i-1] == "c" or strList[i-1] == "d":
                ans -=1
        except:
            continue
        
    elif strList[i] == "j":
        try:
            if strList[i-1] == "l" or strList[i-1] == "n":
                ans -=1
        except:
            continue

print(ans)