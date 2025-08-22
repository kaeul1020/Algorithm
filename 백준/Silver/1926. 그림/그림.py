from collections import deque

N, M = map(int, input().split(" "))
maps = []
for n in range(N):
    maps.append(list(map(int, input().split(" "))))

cnt, max_v = 0, 0
visited = [[False for _ in range(M)] for _ in range(N)]
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

for n in range(N):
    for m in range(M):
        if maps[n][m] == 1:
            if visited[n][m]:
                continue
            cnt += 1
            v = 1
            visited[n][m] = True
            q = deque([(n,m)])
            while q :

                cy, cx = q.popleft()

                for i in range(4):
                    ny, nx = cy+dy[i], cx+dx[i]
                    if 0 <= ny < N and 0 <= nx < M :
                        if maps[ny][nx]==1 and not visited[ny][nx]:
                            visited[ny][nx] = True
                            q.append((ny, nx))
                            v += 1
            max_v = max(max_v, v)

print(cnt)
print(max_v)