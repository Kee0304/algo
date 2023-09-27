import sys
input = sys.stdin.readline

n = int(input())

arr = {0:0, 1:0, 2:1, 3:1}

def dp(n):
    if n in list(arr.keys()):
        return arr[n]
    
    if n % 6 == 0:
        arr[n] = min(dp(n//3), dp(n//2)) + 1

    elif n % 3 == 0:
        arr[n] = min(dp(n//3), dp(n-1)) + 1

    elif n % 2 == 0:
        arr[n] = min(dp(n//2), dp(n-1)) + 1

    else:
        arr[n] = dp(n-1) + 1
    return arr[n]

print(dp(n))