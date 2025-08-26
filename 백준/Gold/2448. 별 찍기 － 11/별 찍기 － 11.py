N = int(input())

stars = [0 for _ in range(N+1)]

def star(n):
    if n <= 3:
        arr = [[' ', ' ', '*', ' ', ' '],
               [' ', '*', ' ', '*', ' '],
               ['*' for _ in range(5)]]
        stars[n] = arr 
        return arr 
    
    result = []
    if stars[n//2] == 0:
        mini_star = star(n//2)
    else : 
        mini_star = stars[n//2]
        
    for top in mini_star:
        result.append([' '*(n//2)] + top + [' '*(n//2)])
    for bottom in mini_star:
        result.append(bottom + [' '] + bottom)
    
    if stars[n] ==0 : 
        stars[n] = result
    return result 

result = star(N)
for i in range(len(result)):
    for j in range(len(result[i])):
        print(result[i][j], end='')
    print('')