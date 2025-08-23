from collections import deque

N, K = map(int, input().split())
visited = [ False for _ in range(100001)]

q = deque([(N, 0)])

if N >= K :
    print(N-K)
else:
    while q :
        cur, sec = q.popleft()
        if cur == K:
            print(sec)
            break

        for i in [cur-1, cur+1, cur*2]:
            if 0 <= i < min(K*2, 100001) and visited[i] == False :
                visited[i] = True
                q.append((i, sec+1))