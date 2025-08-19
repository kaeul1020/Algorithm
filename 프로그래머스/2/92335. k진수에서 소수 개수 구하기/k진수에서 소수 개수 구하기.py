import math

def k_transform(k, n):
    answer = ''
    while n > 0 :
        answer = str(n%k) + answer
        n = n//k
    return answer

def is_prime(n):
    if n == 1:
        return False
    for i in range(2,int(math.sqrt(n))+1):
        if n%i == 0:
            return False
    return True
        

def solution(n, k):

    answer_candi = k_transform(k,n).split("0")

    cnt = 0
    for candi in answer_candi:
        if candi == "":
            continue
        if is_prime(int(candi)):
            cnt+=1
    
    return cnt