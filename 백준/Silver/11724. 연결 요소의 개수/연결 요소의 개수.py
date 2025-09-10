import sys
from collections import deque

N, M = map(int, sys.stdin.readline().rstrip().split())

visited = [ False for _ in range(N+1)]
graph = [[] for _ in range(N+1)]

for _ in range(M):
    u, v = map(int, sys.stdin.readline().rstrip().split())
    graph[u].append(v)
    graph[v].append(u)
    
cnt = 0
for i in range(1, N+1):
    if visited[i]:
        continue
    cnt += 1
    visited[i] = True
    q = deque([i])
    while q :
        cn = q.popleft()
        for nn in graph[cn]:
            if visited[nn]:
                continue
            visited[nn] = True
            q.append(nn)
    
print(cnt)   