from collections import deque

M, N, H = map(int, input().split())

box = [[list(map(int, input().split()))  for _ in range(N)] for _ in range(H)]

# 위, 아래, 왼쪽, 오른쪽, 앞, 뒤 
dm = [0,0,-1,1,0,0]
dn = [0,0,0,0,1, -1]
dh = [-1,1,0,0,0,0]

q = deque([])
answer = 0
cnt = 0

for h in range(H):
    for n in range(N):
        for m in range(M):
            if box[h][n][m] == 1 :
                q.append((h,n,m))
            if box[h][n][m] == 0 :
                cnt += 1

while q :
    ch, cn, cm = q.popleft()
    for i in range(6):
        nh, nn, nm = ch+dh[i], cn+dn[i], cm+dm[i]
        if not(0 <= nh < H and 0<= nn < N and 0<= nm < M):
            continue
        if box[nh][nn][nm] != 0 :
            continue
        cnt -= 1
        answer = box[ch][cn][cm] + 1
        box[nh][nn][nm] = box[ch][cn][cm] + 1
        q.append((nh, nn, nm))

if cnt == 0 and answer == 0:
    print(answer)
elif cnt != 0:
    print(-1)
else:
    print(answer-1)