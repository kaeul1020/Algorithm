def solution(num):
    result = 0
    for _ in range(500):
        if num == 1 :
            return result
        
        result+=1
        if num%2==0:
            num = num/2
        else :
            num = num*3+1
    
    return -1