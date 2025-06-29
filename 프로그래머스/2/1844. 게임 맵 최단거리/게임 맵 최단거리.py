from collections import deque

def solution(maps):
    
    m, n = len(maps), len(maps[0])
    visited = [[False for _ in range(n)] for _ in range(m)]
    visited[0][0] = 1
    q = deque([[0,0]])
    
    dy = [-1,1,0,0]
    dx = [0,0,-1,1]
    
    while q :
        y, x = q.popleft()
        count=visited[y][x]
        
        for i in range(4):
            ny, nx = y+dy[i], x+dx[i]
            
            if (0<=ny<m) and (0<=nx<n) and (maps[ny][nx]==1)and visited[ny][nx] == False:
                q.append([ny, nx])
                visited[ny][nx] = count+1
                
    if visited[m-1][n-1]:
        return visited[m-1][n-1]
    return -1