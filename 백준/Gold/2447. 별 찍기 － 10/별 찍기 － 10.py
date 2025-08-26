N = int(input())

def star(n):
    if n <= 1:
        arr = [['*']]
        return arr
    
    result = []
    for i in range(3):
        arrs = []
        for j in range(3):
            if i==1 and j==1:     
                arrs.append([[' ' for _ in range(n//3)] for _ in range(n//3)])
            else : 
                arrs.append(star(n//3))
        for a1, a2, a3 in zip(*arrs):
            result.append(a1+a2+a3)
    return result

result = star(N)

for i in range(N):
    for j in range(N):
        print(result[i][j], end='')
    print('')