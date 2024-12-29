def solution(n):
    answer = [[0]*n for _ in range(n)]
    d1 = [ 0, 1, 0, -1]
    d2 = [ 1, 0, -1, 0]
    
    i, x, y, d = 1, 0, 0, 0

    while i < n**2+1:

        if (x<0 or x>n-1) or (y<0 or y>n-1) or (answer[x][y] != 0) :
            x -= d1[d%4]
            y -= d2[d%4]
            d += 1
        else : 
            answer[x][y] = i
            i += 1
            
        x += d1[d%4]
        y += d2[d%4]
        
    return answer