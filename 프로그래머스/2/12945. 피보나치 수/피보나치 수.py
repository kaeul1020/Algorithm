def solution(n):
    
    fibo = [0 for _ in range(100001)]
    fibo[1] = 1
    
    for i in range(2, n+1):
        fibo[i] = fibo[i-1]+fibo[i-2] 
    
    return fibo[n]%1234567