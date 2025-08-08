from collections import Counter

def direct(d):
    if d == 'U':
        return (0, 1)
    elif d == 'D':
        return (0, -1)
    elif d == 'L' :
        return (-1, 0)
    else :
        return (1, 0)

def solution(dirs):
    answer = 0

    visited = Counter()
    cx, cy = 0, 0
    
    for d in dirs:
        dx, dy = direct(d)
        nx, ny = cx+dx, cy+dy
        
        if not (-6 < nx < 6 and -6 < ny < 6):
            continue
        
        visited[(cx,cy,nx,ny)] = 1
        visited[(nx,ny,cx,cy)] = 1
        
        cx, cy = nx, ny

    return len(visited)//2