from collections import deque

def solution(n, computers):

    visited = [ False for _ in range(n) ]
    cnt = 0
    for s in range(n):
        if visited[s]:
            continue

        cnt += 1
        visited[s] = True
        q = deque([s])
        while q:
            cur = q.popleft()
            for e in range(n):
                if computers[e][cur] == 1 and not visited[e] :
                    visited[e] = True
                    q.append(e) 

    return cnt