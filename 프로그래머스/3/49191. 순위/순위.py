from collections import deque

def bfs(n, i, graph):
    dist= [False] * (n+1)
    dist[i] = True
    
    q = deque([i])
    while q:
        cur = q.popleft()
        for nxt in graph[cur]:
            if dist[nxt] == False:
                q.append(nxt)
                dist[nxt] = True
            
    return sum(dist)-1

def solution(n, results):
    
    win_graph = [[] for _ in range(n+1)]
    lose_graph = [[] for _ in range(n+1)]
    
    for u, v in results:
        win_graph[u].append(v)
        lose_graph[v].append(u)
    
    count = 0
    
    for i in range(1, n+1):
        wins = bfs(n, i, win_graph)
        loses = bfs(n, i, lose_graph)
        
        if wins+loses == n-1:
            count +=1        
    
    return count