from collections import deque

def solution(n, computers):
    
    graph = [[] for _ in range(n)]
    
    for i in range(len(computers)):
        for j in range(len(computers[i])):
            if computers[i][j] and i!=j:
                graph[i].append(j)
    
    dist = [ True for _ in range(n)]
    
    count = 0
    
    for i in range(n):
        if dist[i]:
            q = deque([i])
            while q :
                cur = q.popleft()
                if dist[cur] and graph[cur]!=[]:
                    for i in graph[cur]:
                        if dist[i]:
                            q.append(i)
                    
                    dist[cur] = False
            count += 1        
    
    
    return count