from collections import deque

T = int(input())
for _ in range(T):
    I = int(input())
    board = [[0 for _ in range(I)] for _ in range(I)]
    cx, cy = map(int, input().split())
    tx, ty = map(int, input().split())
    
    # 1시방향부터 시계방향으로
    dx = [1, 2, 2, 1, -1, -2, -2, -1]
    dy = [-2, -1, 1, 2, 2, 1, -1, -2]
    
    board[cx][cy] = 1
    q = deque([(cx,cy)])
    while q :
        cx, cy = q.popleft()
        
        if (tx, ty) == (cx, cy):
            print(board[cx][cy]-1)
            break
        
        for i in range(8):
            nx = cx+dx[i]
            ny = cy+dy[i]
            
            if not(0<=nx<I and 0<=ny<I and board[nx][ny]==0):
                continue
            
            board[nx][ny] = board[cx][cy] + 1
            q.append((nx, ny))