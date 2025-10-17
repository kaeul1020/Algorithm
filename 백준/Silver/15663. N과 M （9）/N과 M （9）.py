from itertools import permutations

N, M = map(int, input().split())
cand = list(map(int,input().split()))

result = set([])
for i in permutations(cand, M):
    result.add(i)
    
result = list(result)
result.sort()
for i in result:
    print(*i)