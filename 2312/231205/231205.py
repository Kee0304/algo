import sys
input = sys.stdin.readline

N = int(input())
input_list = list(map(int,input().split()))

def findIndex(targetNum):
    start, end = 0, len(LIS)-1
    while start<end:
        mid = (start+end)//2
        if LIS[mid] < targetNum:
            start = mid+1
        elif LIS[mid] > targetNum:
            end = mid
        else:
            start = mid
            end = mid
    return start

def findIndex2(targetNum):
    start, end = 0, len(LDS)-1
    while start<end:
        mid = (start+end)//2
        if LDS[mid] < targetNum:
            end = mid
        elif LDS[mid] > targetNum:
            start = mid+1
        else:
            start = mid
            end = mid
    return start

max_len = 0

for i in range(N):
    point = input_list[i]
    LIS = [input_list[0]]
    LDS = [point]
    
    for j in range(N):
        num = input_list[j]
        
        if j<=i:
            if LIS[-1] < num:
                LIS.append(num)
            elif LIS[-1] > num :
                LIS[findIndex(num)] = num
        else:
            if LDS[-1] > num:
                LDS.append(num)
            elif LDS[-1] < num:
                LDS[findIndex2(num)] = num

    bitonic_len = len(LIS) + len(LDS) -1
    if max_len < bitonic_len:
        max_len = bitonic_len

print(max_len)