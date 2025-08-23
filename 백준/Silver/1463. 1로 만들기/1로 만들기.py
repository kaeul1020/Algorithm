from collections import deque
n = int(input())

visited = [False for _ in range(n+1)]
visited[n] = 1
q = deque([n])
while q:
    x = q.popleft()
    if x == 1:
        break
    
    if x%3 == 0 and not visited[x//3]:
        visited[x//3] = visited[x]+1
        q.append(x//3)
    if x%2 == 0 and not visited[x//2]:
        visited[x//2] = visited[x]+1
        q.append(x//2)
    if x-1 > 0 and not visited[x-1]:
        visited[x-1] = visited[x]+1
        q.append(x-1)

print(visited[1]-1)