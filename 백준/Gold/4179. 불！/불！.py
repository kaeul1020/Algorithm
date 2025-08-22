from collections import deque

R, C = map(int, input().split())

dy = [-1,1,0,0]
dx = [0,0,-1,1]

q = deque([])
maze = []
for _ in range(R):
    maze.append(list(input()))

for r in range(R):
    for c in range(C):
        if maze[r][c] == "F":
            q.append(("F", r, c))
        elif maze[r][c] == "J":
            maze[r][c] = 0
            q.appendleft(("J", r, c))
# print(q)
answer = 0
while q and answer == 0: 
    cmd, cy, cx = q.popleft()
    if maze[cy][cx] == "F" and cmd == "J":
        continue
    
    for i in range(4):
        ny, nx = cy+dy[i], cx+dx[i]            
        if not (-1 < ny < R and -1 < nx < C):
            if cmd == "J":
                answer = maze[cy][cx] + 1
                break
            else : continue

        if cmd == "J" and maze[ny][nx] == ".":
            maze[ny][nx] = maze[cy][cx] + 1
            q.append(("J", ny, nx))
            
        elif cmd == "F" and (maze[ny][nx] not in ["F","#"]):
            maze[ny][nx] = "F"
            q.append(("F", ny, nx))
    # for m in maze :
    #     print(m)
    # print(q)
    # print("")

if answer == 0 :
    answer = "IMPOSSIBLE"

print(answer)