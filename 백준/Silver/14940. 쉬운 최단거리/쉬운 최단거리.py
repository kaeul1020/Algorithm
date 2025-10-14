from collections import deque

N, M = map(int, input().split())
sn, sm = 0,0

land = []
for n in range(N):
    row = list(map(int,input().split()))
    for m, r in enumerate(row) :
        if r == 2:
            sn, sm = n, m 
    land.append(row)

# 장애물은 0, 땅은 1, 출발점은 2

dn = [-1,1,0,0]
dm = [0,0,-1,1]

result = [[-1 for _ in range(M)] for _ in range(N)]

q = deque([(sn, sm)])
result[sn][sm] = 0

while q :
    cn, cm = q.popleft()
    
    for i in range(4):
        nn, nm = cn+dn[i], cm+dm[i]
        if not (0 <= nn < N and 0 <= nm < M and result[nn][nm] == -1 and land[nn][nm] == 1) :
            continue
        q.append((nn, nm))
        result[nn][nm] = result[cn][cm]+1

for n in range(N):
    for m in range(M):
        if land[n][m] == 0:
            print(0, end=" ")
        else:
            print(result[n][m], end=" ")
        
    print("")