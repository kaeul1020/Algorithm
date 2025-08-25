N = int(input())

paper = []
for _ in range(N):
    paper.append(list(map(int, input().split())))

def full(n, arr):
    answer_dic = {0 : 0, -1:0, 1:0}
    
    check = arr[0][0]
    flag = True
    k = 0
    while flag and k < n*n :
        i = k//n
        j = k%n
        if check!=arr[i][j]:
            flag = False
        k += 1
    
    if flag : 
        answer_dic[check] += 1
        return answer_dic

    split = [0, n//3, (n//3)*2, n]
    for i in range(3):
        for j in range(3):
            full_dic = full(n//3, [row[split[j]:split[j+1]] for row in arr[split[i]:split[i+1]]])
            
            for k, v in full_dic.items():
                answer_dic[k] += v
    return answer_dic

answer = full(N,paper)
print(answer[-1])
print(answer[0])
print(answer[1])