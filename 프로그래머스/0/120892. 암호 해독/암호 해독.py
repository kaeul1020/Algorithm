def solution(cipher, code):
    answer = ''
    for i, c in enumerate(cipher):
        if i%code==code-1:
            answer+=c
        
    return answer