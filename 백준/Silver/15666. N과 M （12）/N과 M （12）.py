from itertools import combinations_with_replacement

N, M = map(int, input().split())

cand = list(set(map(int, input().split())))
cand.sort()

for i in combinations_with_replacement(cand, M):
    print(*i)