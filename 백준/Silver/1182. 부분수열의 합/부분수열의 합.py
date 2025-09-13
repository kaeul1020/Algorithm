N, S = map(int, input().split())
ps = list(map(int, input().split()))
visited = [False for _ in range(N)]

def check(start, cur_s):
    cnt = 0
    for i in range(start,N):
        if not visited[i]:
            visited[i] = True
            cur_s += ps[i]
            if S == cur_s:
                cnt+=1
            cnt += check(i+1, cur_s)
            visited[i] = False
            cur_s -= ps[i]
    return cnt
            
print(check(0,0))