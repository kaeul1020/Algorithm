def solution(my_string):
    answer = []
    
    z2n = [str(i) for i in range(0, 10)]
    
    for s in my_string:
        if s in z2n:
            answer.append(int(s))
    
    answer.sort()
    
    return answer