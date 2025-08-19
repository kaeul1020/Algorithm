def solution(emergency):
    answer = [ 0 for _ in range(len(emergency))]
    emergency = [(e, idx) for idx, e in enumerate(emergency)]
    emergency.sort(reverse=True)
    
    rank = 1
    for _, idx in emergency:
        answer[idx] = rank
        rank+=1

    return answer