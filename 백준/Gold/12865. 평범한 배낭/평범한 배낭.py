N, K = map(int, input().split())
items = []

for _ in range(N):
    w, v = map(int, input().split())
    if w <= K:
        items.append((w,v))
        
dp = [0 for _ in range(K+1)]

for w, v in items:
    for cap in range(K, w-1, -1):
        cand = dp[cap-w] + v
        if cand > dp[cap]:
            dp[cap] = cand
            
print(dp[-1])