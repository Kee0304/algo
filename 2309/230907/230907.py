import sys
inp = sys.stdin.readline

# 3*3 배열 A
# [[1],[2],[3]]
# [[2],[4],[6]]
# [[3],[6],[9]]

# A의 원소를 전부 다 일차원 배열 B에 때려넣고 B를 오름차순으로 정렬

# N이 10**5이기 때문에 for로 직접 전부 때려 넣으면 최악의 경우 10**10=100억


# 수는 N**N 범위 내에서 약수 중 수를 약수로 나눈 결과도 N보다 작은 약수의 수 만큼 존재

def divisor(num, N):
    divisorList = []

    for i in range(1, int(num**(1/2))+1):
        if (num%i) == 0:
            if (i <= N) and (num//i <= N):
                divisorList.append(i)
                if (i**2 != num):
                    divisorList.append(num//i)
    
    return len(divisorList)

N = int(inp())
k = int(inp())

cnt = 0
num = 1

while cnt<k:
    cnt += divisor(num, N)
    num+=1
num-=1
print(num)