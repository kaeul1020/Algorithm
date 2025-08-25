N = int(input())

paper = []
for _ in range(N):
    paper.append(list(map(int, input().split())))
    
def split(n, arr):
    sum_arr = 0
    for a in arr:
        sum_arr+= sum(a)
    answer = [0, 0]
    if sum_arr == 0 or sum_arr == n*n:
        answer[sum_arr//(n*n)] += 1
        return answer
    
    loc = [0, n//2, n]
    for i in range(2):
        for j in range(2):
            split_arr = [row[loc[j]:loc[j+1]] for row in arr[loc[i]:loc[i+1]]]
            split_answer = split(n//2, split_arr)
            answer = [i+j for i,j in zip(answer, split_answer)]
            
    return answer

answer = split(N, paper)
print(answer[0])
print(answer[1])