def solution(msg):
    answer = []
    
    voc = [""]
    
    for alpha in range(ord("A"), ord("Z")+1):
        voc.append(chr(alpha))
    
    idx = 0
    while idx < len(msg):
        n_idx = idx
        while msg[idx:n_idx] in voc and n_idx < len(msg):
            n_idx += 1
            
        if msg[idx:n_idx] in voc:
            answer.append(voc.index(msg[idx:n_idx]))
            idx = n_idx
            
        else : 
            answer.append(voc.index(msg[idx:n_idx-1]))
            voc.append(msg[idx:n_idx])
        
            idx = n_idx-1


    return answer