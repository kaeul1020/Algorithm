def solution(N, number):
    
    dp = [set() for _ in range(9)]
    
    for k in range(1,9):
        dp[k].add(int(str(N)*k))
        
        for i in range(1,k):
            j = k-i
            for x in dp[i]:
                for y in dp[j]:
                    dp[k].add(x+y)
                    dp[k].add(x-y)
                    dp[k].add(x*y)
                    if y!=0:
                        dp[k].add(x//y)
        if number in dp[k]:
            return k
    
    
    return -1