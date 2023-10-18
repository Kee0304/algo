import sys
input = sys.stdin.readline
print = sys.stdout.write

def multi(num, mul):
    if mul == 1:
        return num%C
    
    tmp = multi(num,mul//2)

    # 나누기 분배 법칙
    # (A*B)%p = ((A%P)*(B%P))%P
    if mul%2 == 0:
        return (tmp*tmp)%C
        
    else:
        return (tmp*tmp*num)%C


A,B,C = map(int,input().split())
ans = multi(A,B)

print(str((ans)))