N = int(input())
Ps = list(map(int, input().split()))

Ps.sort()
for idx in range(1, len(Ps)):
    Ps[idx] += Ps[idx-1]

print(sum(Ps))