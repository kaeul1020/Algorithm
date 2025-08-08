from collections import deque

def solution(priorities, location):

    q = deque((idx, p) for idx, p in enumerate(priorities))
    
    max_stack = sorted(priorities)
    print(max_stack[-1])
    cnt = 1
    
    while q :
        i, cur = q.popleft()
        if max_stack[-1] == cur :
            max_stack.pop()
            
            if i == location :
                return cnt
            
            cnt += 1
            
        else :
            q.append((i, cur))
            
    return cnt