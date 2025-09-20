import sys
N, M = map(int, input().split())

table = [[0 for _ in range(N+1)] for _ in range(N+1)]
for i in range(1,N+1):
    for j, v in enumerate(list(map(int, sys.stdin.readline().rstrip().split()))):
        j += 1
        table[i][j] = v + table[i-1][j] + table[i][j-1] - table[i-1][j-1]


for _ in range(M):
    x1,y1,x2,y2 = map(int,sys.stdin.readline().rstrip().split())
    x1-=1
    y1-=1
    answer = table[x2][y2] - table[x2][y1] - table[x1][y2] + table[x1][y1]
    print(answer)
