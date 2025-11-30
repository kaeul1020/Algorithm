from collections import Counter
N = int(input())
cnt = Counter()
for n in list(map(int,input().split())):
    cnt[n] += 1

M = int(input())
answer = []
for m in list(map(int,input().split())):
    answer.append(cnt[m])

print(*answer)