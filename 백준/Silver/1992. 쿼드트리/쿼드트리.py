N = int(input())

video = []
for _ in range(N):
    video.append(list(map(int, input())))

def quad_tree(n, arr):
    flag, k, comp = True, 0, arr[0][0]
    while flag and k < n*n :
        i, j = k//n, k%n
        if comp != arr[i][j]:
            flag = False
        k+=1

    if flag :
        return str(comp)
    
    answer = "("
    loc = [0, n//2, n]
    for i in range(2):
        for j in range(2):
            answer+= quad_tree(n//2, [row[loc[j]:loc[j+1]] for row in arr[loc[i]:loc[i+1]]])
    answer += ")"
    return answer

print(quad_tree(N, video)) 