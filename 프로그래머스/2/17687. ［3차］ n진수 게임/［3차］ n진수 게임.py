def n_transform(n, number):
    
    if number == 0 : 
        return "0"
    
    n_voc = {10 : "A",
            11 : "B", 
            12 : "C",
            13 : "D",
            14 : "E",
            15 : "F"}
    
    answer = ""
    while number > 0:
        
        new_answer = number % n
        
        if 10 <= new_answer <= 15:
            answer = str(n_voc[new_answer]) + answer
        else : 
            answer = str(new_answer) + answer
        number = number // n
    
    return answer


def solution(n, t, m, p):
    answer = ''
    
#     n진법 구하는 함수 따로 빼기
#     str 길이를 m*(t-1) + p 만큼 얻는다.
    i = 0
    while len(answer) < m*(t-1) + p :
        answer += n_transform(n, i)
        i += 1
    
#     index로 접근해서 출력한다.
    
    return "".join([answer[m*t_idx+p-1] for t_idx in range(t)])