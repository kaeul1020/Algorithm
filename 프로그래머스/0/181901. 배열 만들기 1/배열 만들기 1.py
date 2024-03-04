def solution(n, k):
    answer = []
    i = 1
    
    while i*k <= n:
        answer.append(i*k)
        i+=1
    
    return answer