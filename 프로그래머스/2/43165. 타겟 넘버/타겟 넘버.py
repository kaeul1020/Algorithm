from collections import deque

def solution(numbers, target):
    
    checks = [[] for _ in range(len(numbers)+1)]
    checks[0].append(0)
    
    for i, n in enumerate([0]+numbers):
        if i == 0 : continue
        for c in checks[i-1]:
            checks[i].append(c+n)
            checks[i].append(c-n)
    
    return checks[-1].count(target)