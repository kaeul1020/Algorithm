import sys, heapq

N = int(input())
M = int(input())

graph = [[] for _ in range(N+1)]
dist=[1000000*1000 for _ in range(N+1)]

for _ in range(M):
    start, end, value = map(int, sys.stdin.readline().rstrip().split())
    graph[start].append((value, end))


s, e = map(int, sys.stdin.readline().rstrip().split())

q = [(0, s)]
dist[s] = 0
while q:
    cv, cs = heapq.heappop(q)
    if cs == e:
        print(dist[e])
        break
    
    if cv > dist[cs]:
        continue
    
    for nv, ns in graph[cs]:
        if cv+nv < dist[ns]:
            dist[ns] = cv+nv
            heapq.heappush(q, (cv+nv, ns))