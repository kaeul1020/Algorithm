def solution(m, n, puddles):
    
    puddles = [[y-1, x-1] for x, y in puddles]
    
    maps = [[0 for _ in range(m)] for _ in range(n)]
    
    for y in range(n):
        for x in range(m):
            if (y, x) == (0,0):
                maps[y][x] = 1
                continue
            if [y,x] in puddles:
                maps[y][x] = -1
                continue
                
            sum_list = [0]
            if 0 <= y-1 and (maps[y-1][x] != -1):
                sum_list.append(maps[y-1][x])
            if 0 <= x-1 and (maps[y][x-1] != -1):
                sum_list.append(maps[y][x-1])
            
            maps[y][x] += sum(sum_list)
            
    return maps[-1][-1] % 1000000007