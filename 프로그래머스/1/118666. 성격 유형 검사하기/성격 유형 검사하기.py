def solution(survey, choices):
    answer = ''
    scores = {"RT":0,
             "CF":0,
             "JM":0,
             "AN":0}
    
    for s, c in zip(survey, choices):
        
        c = c-4
        if s not in list(scores.keys()):
            c *= -1
            s = s[::-1]
            
        scores[s] += c

    for t, score in scores.items():
        if score <= 0 :
            answer+= t[0]
        else :
            answer+= t[1]
        
    
    return answer