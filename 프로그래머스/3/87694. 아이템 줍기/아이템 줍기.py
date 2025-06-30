from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
       
    maps = [[False for _ in range(101)] for _ in range(101)]
    dist = [[0 for _ in range(101)] for _ in range(101)]
    
    for lx, ly, rx, ry in rectangle:
        lx, ly, rx, ry = lx*2, ly*2, rx*2, ry*2 
        for i in range(lx, rx+1):
            maps[ly][i], maps[ry][i] = True, True
        for i in range(ly, ry+1):
            maps[i][lx], maps[i][rx] = True, True
            
    for lx, ly, rx, ry in rectangle:
        lx, ly, rx, ry = lx*2, ly*2, rx*2, ry*2 
        for j in range(ly+1, ry):
            for i in range(lx+1, rx):
                maps[j][i] = False
                
    # for i in range(10,-1,-1):
    #     for value in maps[i][:10]:
    #         print(int(value), end="")
    #     print("")
    
    characterX, characterY, itemX, itemY = characterX*2, characterY*2, itemX*2, itemY*2

    q = deque([(characterY, characterX)])
    dist[characterY][characterX] = 1
    
    dy = [-1,1,0,0]
    dx = [0,0,-1,1]
    
    while q:
        cy,cx = q.popleft()
        for i in range(4):
            ny, nx = cy+dy[i], cx+dx[i]
            if 0<nx<101 and 0<ny<101 and maps[ny][nx] and dist[ny][nx]==0 :
                dist[ny][nx] = dist[cy][cx]+1
                if nx == itemX and ny == itemY:
                    return dist[itemY][itemX]//2
                q.append((ny,nx))
                
    return dist[itemY][itemX]//2