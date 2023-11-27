import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
part = [A[0]]

def findIndex(targetNum):
    start, end = 0, len(part)-1
    while start<end:
        mid = (start+end)//2
        if part[mid] < targetNum:
            start = mid+1
        elif part[mid] > targetNum:
            end = mid
        else:
            start = mid
            end = mid
    return start


for num in A:
    # 가장 큰 값이 들어오면
    if part[-1] < num:
        # 그냥 추가
        part.append(num)
    # 그렇지 않으면
    else:
        # 자리를 찾아준다
        part[findIndex(num)] = num

print(len(part))