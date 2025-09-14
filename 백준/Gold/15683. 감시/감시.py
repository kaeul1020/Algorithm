import copy

N, M = map(int, input().split())
cctv, graph = [], []
mode = [
    [],
    [[0],[1],[2],[3]],
    [[2,3],[0,1]],
    [[3,0], [0,2], [2,1], [1, 3]],
    [[3,0,2],[0,2,1],[2,1,3], [0,3,1]],
    [[0,1,2,3]]
]

# 상 하 좌 우
dx = [0,0,-1,1]
dy = [-1,1,0,0]

for i in range(N):
    graph.append(list(map(int,input().split()))) 
    for j in range(M):
        cctv_num = graph[i][j]
        if cctv_num in range(1,6):
            cctv.append((cctv_num, i,j))


def fill(arr, mode_di, x, y):
    for i in mode_di:
        nx, ny = x+dx[i], y+dy[i]
        while 0 <= nx < M and 0 <= ny < N and arr[ny][nx] != 6:
            if arr[ny][nx] == 0:
                arr[ny][nx] = "#"
            nx, ny = nx+dx[i], ny+dy[i]

def DFS(depth, min_zero, arr):
    if depth == len(cctv):
        cnt = 0
        for n in range(N):
            cnt += arr[n].count(0)
        return min(min_zero, cnt)
    cctv_num, y, x = cctv[depth]
    for m in mode[cctv_num]:
        temp = copy.deepcopy(arr)
        fill(temp, m, x, y)
        min_zero = DFS(depth+1, min_zero, temp)
        
    return min_zero

print(DFS(0, N*M+1, graph))      