N, K = map(int, input().split())

A = []
for _ in range(1,N+1):
    A.append(int(input()))

cnt = 0
for a in sorted(A, reverse=True):
    if a > K :
        continue
    
    cnt += K//a
    K = K%a

print(cnt)