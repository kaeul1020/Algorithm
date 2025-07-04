def solution(brown, yellow):
    answer = []
    
    total = brown + yellow
    
    candi = []
    i =3
    while total//i >= i:
        if total % i == 0 and (total//i-2)*(i-2) == yellow:
            return [total//i, i]
        i += 1
    return answer