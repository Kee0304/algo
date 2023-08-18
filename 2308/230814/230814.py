import sys
inp = sys.stdin.readline

# 숫자 0~N-1
N = int(inp())

# 인덱스 번호에 따른 숫자의 가격
roomNumList = list(map(int,inp().split()))

# 소지금
M = int(inp())

# index = 돈에 대해서 살 수 있는 가장 큰 방 번호를 저장하는 리스트
possibleMax = [-51 for _ in range(M+1)]

# 큰 숫자부터 돌면서
for room in range(N-1, -1, -1):
    roomCost = roomNumList[room]
    # 그 숫자에 해당하는 방을 살 수 있는 돈으로 살 수 있는 최대의 방 숫자를 구한다
    for money in range(roomCost, M+1):
        # 최대의 방 숫자 =
        # 1. possibleMax[money] = money로 살 수 있는 가장 큰 방 번호
        # 2. room = 지금 순회하고 있는 방 번호
        # 3. possibleMax[money - roomCost]*10 + room = 지금 순회하는 방 번호를 사서 맨 뒤에 붙인 방 번호
        # 중 가장 큰 값으로 갱신
        possibleMax[money] = max(possibleMax[money], room, possibleMax[money-roomCost]*10+room)

print(possibleMax[M])