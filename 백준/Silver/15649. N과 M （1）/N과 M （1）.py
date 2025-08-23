from itertools import permutations

N, M = map(int, input().split())

for answer in permutations([i for i in range(1, N+1)], M):
    print(*answer)