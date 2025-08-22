from collections import deque

N, M = map(int, input().split(" "))
maze = []
for _ in range(N):
    maze.append(list(map(int, input())))
    
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

maze[0][0] += 1
q = deque([(0, 0)])

while q:
    cy, cx = q.popleft()
    for i in range(4):
        ny, nx = cy+dy[i], cx+dx[i]
        if -1 < ny < N and -1 < nx < M :
            if maze[ny][nx] == 1:
                maze[ny][nx] = maze[cy][cx] + 1
                q.append((ny, nx))
print(maze[N-1][M-1]-1)