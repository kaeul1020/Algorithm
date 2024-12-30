def solution(N, stages):
    fail = {}
    total = len(stages)
    for i in range(1,N+1):
        try :
            fail[str(i)] = stages.count(i) / total
            total -= stages.count(i)
        except :
            fail[str(i)] = 0
    fail = sorted(fail.items(), key = lambda item:item[1], reverse=True)
    
    return [int(i) for i, _ in fail]