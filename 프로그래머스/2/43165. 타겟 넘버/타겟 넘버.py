def solution(numbers, target):
    answer = 0
    
    def dfs(i, cur):
        cnt = 0
        
        if i == len(numbers):
            return int(cur==target)
        
        cnt += dfs(i+1, cur+numbers[i])
        cnt += dfs(i+1, cur-numbers[i])
        
        return cnt 
        
    
    answer += dfs(0, 0)
    
    return answer