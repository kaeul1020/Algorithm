def solution(n, words):
    
    history = []
    
    for i, w in enumerate(words):
        
        if history == [] :
            history.append(w)
            continue
        
        if w in history or history[-1][-1] != w[0]:
            return [i%n +1, i//n +1]
        
        history.append(w)

    return [0,0]