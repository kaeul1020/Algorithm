def solution(arr):
    answer = []
    for a in arr:
        if answer == []:
            answer.append(a)
        elif a != answer[-1]:
            answer.append(a)
        
    
    return answer