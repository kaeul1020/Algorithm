
N = int(input())

U = [int(input()) for _ in range(N)]
U.sort()


sums = set()
for i in range(N):
    for j in range(N):
        if U[i]+U[j] >= U[-1]:
            continue
        sums.add(U[i]+U[j])
        
flag = False
answer = -1
for ki in range(N-1, -1, -1):
    k = U[ki]
    for ui in range(N):
        target = k - U[ui]
        flag = target in sums
        if flag : 
            answer = k
            break
    if flag : break

print(k)