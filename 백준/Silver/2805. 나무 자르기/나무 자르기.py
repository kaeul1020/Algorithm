N, M = map(int,input().split())
trees = list(map(int,input().split()))

top, bottom = max(trees), 0
answer = 0
while bottom <= top:
    mid = (top + bottom) // 2
    
    total = sum([max(0, tree-mid) for tree in trees])
    
    if total >= M:
        answer = mid
        bottom = mid+1
    else:
        top = mid - 1
    
print(answer)