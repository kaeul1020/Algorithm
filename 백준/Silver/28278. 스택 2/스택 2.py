N = int(input())

results = []
stack = []

for _ in range(N):
    
    order = list(map(int, input().split(' ')))

    if order[0] == 1:
        stack.append(order[1])
        continue
    if order[0] == 2 : 
        if len(stack) != 0:
            results.append(stack.pop())
        else:
            results.append(-1)
        continue
    if order[0] == 3:
        results.append(len(stack))
        continue
    if order[0] == 4:
        if len(stack) == 0 :
            results.append(1)
        else: 
            results.append(0)
        continue
    if order[0] == 5:
        if len(stack) != 0:
            results.append(stack[-1])
        else :
            results.append(-1)
        continue

for r in results: print(r)