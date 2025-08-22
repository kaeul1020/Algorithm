from collections import deque

M, N = map(int, input().split())

def in_zero(arr):
    for row in arr:
        if 0 in row:
            return True
    return False

# 1 : 익은 토마토
# 0 : 안익은 토마토
# -1 : 토마토 없음  

dy = [-1, 1, 0, 0]    
dx = [0, 0, -1, 1]
    
warehouse = []
for _ in range(N):
    tomatos = list(map(int, input().split()))
    warehouse.append(tomatos)

if not in_zero(warehouse):
    print(0)    
else:
    max_day = 0
    q = deque([])
    for n in range(N):
        for m in range(M):
            if warehouse[n][m] == 1:
                q.append((n,m))
            
    while q :
        cy, cx = q.popleft()
        for i in range(4):
            ny, nx = cy+dy[i], cx+dx[i]
            if -1 < ny < N and -1 < nx < M and warehouse[ny][nx] == 0:
                warehouse[ny][nx] = warehouse[cy][cx] + 1
                max_day = max(max_day, warehouse[ny][nx])
                q.append((ny, nx))
                
    if in_zero(warehouse):
        print(-1)
    else : 
        print(max_day-1)
