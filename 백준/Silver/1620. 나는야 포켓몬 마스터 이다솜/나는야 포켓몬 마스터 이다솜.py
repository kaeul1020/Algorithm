import sys

N, M = map(int, sys.stdin.readline().split())

voc = {}
for i in range(N):
    name = sys.stdin.readline().strip()
    voc[i+1] = name
    voc[name] = i+1
    

for _ in range(M):
    keyword = sys.stdin.readline().strip()
    if keyword.isalpha():
        print(voc[keyword])
    else:
        print(voc[int(keyword)])