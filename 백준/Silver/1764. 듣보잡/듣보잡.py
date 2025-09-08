import sys

N, M = map(int, input().split())

NotListen = set([sys.stdin.readline().strip() for _ in range(N)])
NotSee = set([sys.stdin.readline().strip() for _ in range(M)])

answer = list(NotListen & NotSee)
answer.sort()

print(len(answer))
for name in answer:
    print(name)
