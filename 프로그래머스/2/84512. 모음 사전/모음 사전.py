from itertools import product

def solution(word):
    answer = 0
    
    voc = []
    
    for i in range(1, 6):
        for v in product(['A', 'E', 'I', 'O', 'U'], repeat=i):
            voc.append("".join(v))
    
    voc.sort()
    
    return voc.index(word)+1