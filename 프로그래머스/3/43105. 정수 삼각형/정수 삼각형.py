def solution(triangle):

    for i in range(1, len(triangle)):
        for j in range(len(triangle[i])): 
            
            if j == 0 :
                comp = triangle[i-1][j]
            elif j == i :
                comp = triangle[i-1][j-1]
            else : 
                comp = max(triangle[i-1][j-1], triangle[i-1][j])
            triangle[i][j] = comp + triangle[i][j]
    
    return max(triangle[-1])