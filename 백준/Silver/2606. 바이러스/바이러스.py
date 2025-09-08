from collections import deque

C = int(input())
connectN = int(input())

coms = [[] for _ in range(C+1)]
visited = [False for _ in range(C+1)]

for _ in range(connectN):
    a, b = map(int, input().split())
    coms[a].append(b)
    coms[b].append(a)
    
visited[1] = True    
q = deque([1])
while q :
    c = q.popleft()
    for nc in coms[c]:
        if visited[nc] == False :
            visited[nc] = True
            q.append(nc)

print(sum(visited)-1)