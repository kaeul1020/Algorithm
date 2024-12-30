def solution(dartResult):
    
    scores = [i for i in range(3)]
    bonus = {'S':1,'D':2,'T':3}

    for i in range(3):
        # 숫자 구별
        if dartResult[1].isdigit():
            scores[i] = int(dartResult[:2])
            dartResult = dartResult[2:]
        else :
            scores[i] = int(dartResult[:1])
            dartResult = dartResult[1:]
        
        
        # 보너스 구별
        scores[i] = scores[i] ** bonus[dartResult[0]]
        dartResult = dartResult[1:]
        
        # 옵션 구별
        if len(dartResult) > 0:
            if dartResult[0] == '#':
                scores[i] *= -1
                dartResult = dartResult[1:]
            elif dartResult[0] == '*':
                scores[i] *= 2
                if i > 0 :
                    scores[i-1] *= 2
                dartResult = dartResult[1:]
    
    return sum(scores)