from collections import deque

def solution(n, edge):
    
    graph = [[] for _ in range(n+1)]
    for u,v in edge:
        graph[u].append(v)
        graph[v].append(u)
    
    dist = [-1] * (n+1)
    dist[1] = 0
    
    q = deque([1])
    while q:
        cur = q.popleft()
        for nxt in graph[cur]:
            if dist[nxt] == -1:
                dist[nxt] = dist[cur] + 1
                q.append(nxt)
    
    return dist.count(max(dist))