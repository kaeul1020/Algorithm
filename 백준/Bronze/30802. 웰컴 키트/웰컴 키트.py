import math
N = int(input())

t_shirts = list(map(int, input().split()))
T, P = map(int, input().split())

print(sum([math.ceil(t_shirt/T) for t_shirt in t_shirts]))
print(N//P, N%P)