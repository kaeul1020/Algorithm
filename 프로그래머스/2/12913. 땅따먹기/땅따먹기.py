def solution(land):
    answer = 0
    prev = land[0]
    for r in range(1, len(land)):
        curs = []
        for i in range(4):
            curs.append(land[r][i] + max(prev[:i]+prev[i+1:]))
        prev = curs
            
    
    
    return max(prev)