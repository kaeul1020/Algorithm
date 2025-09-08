import sys

_, M = map(int, input().split())
Ns = list(map(int, sys.stdin.readline().split()))
sums = [Ns[0]]
for i in range(1,len(Ns)):
    sums.append(sums[-1]+Ns[i])

for _ in range(M):
    s, e = map(int, sys.stdin.readline().split())
    
    if s-2 < 0 :
        print(sums[e-1])  
    else : print(sums[e-1] - sums[s-2])  