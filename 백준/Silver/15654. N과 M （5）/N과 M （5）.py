from itertools import permutations

N, M = map(int, input().split())

cand = list(map(int, input().split()))
cand.sort()

for i in permutations(cand, M):
    print(*i)