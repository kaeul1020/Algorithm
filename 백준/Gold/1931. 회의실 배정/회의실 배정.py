import sys

N = int(sys.stdin.readline().rstrip())
meetings = []
for _ in range(N):
    s, e = map(int, sys.stdin.readline().rstrip().split())
    meetings.append((s,e))
    
meetings.sort(key=lambda x:(x[1], x[0]))

cnt = 1
cur_e = meetings[0][1]
for idx in range(1, N):
    if cur_e <= meetings[idx][0]:
        cnt+=1
        cur_e = meetings[idx][1]
        
print(cnt)