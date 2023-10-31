import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

# 실제 중가하는 부분 수열을 구하는 것이 아니라, 그 길이만 구하면 된다
# 수열에서 현재 최대값보다 큰 값이 들어오면 그냥 추가하고
# 그렇지 않으면 이분탐색으로 자리를 찾아서 대체한다. 
# 즉 실제로 존재할 수 없는 부분 수열이라도 대체를 해서 길이만 같다면 상관 없게 된다

# [10, 20, 50, 70, 30, 35, 80]이라는 수열이 주어졌을 때
# 실제 가능한 수열은 10 20 50 70 80 이지만
# 이 풀이로 10 20 30 35 80 의 길이도 5이다.


# 가상의 부분 수열을 저장할 리스트
part = [A[0]]

# 이분 탐색으로 자리 찾아주기
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
