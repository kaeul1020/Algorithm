from collections import deque

T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split())

    farm = [ [0 for _ in range(M)] for _ in range(N)]
    for _ in range(K):
        x, y = map(int, input().split())
        farm[y][x] = 1
        
    dx = [0,0,-1,1]
    dy = [1,-1,0,0]

    cnt = 0
    for y in range(N):
        for x in range(M):
            if farm[y][x] == 1:
                cnt +=1
                farm[y][x] = 0
                q = deque([(y,x)])            
                while q:
                    cy, cx = q.popleft()
                    for i in range(4):
                        ny, nx = cy+dy[i], cx+dx[i]
                        if not( 0 <= ny < N and 0 <= nx < M and farm[ny][nx]==1):
                            continue
                        farm[ny][nx] = 0
                        q.append((ny, nx))

    print(cnt)