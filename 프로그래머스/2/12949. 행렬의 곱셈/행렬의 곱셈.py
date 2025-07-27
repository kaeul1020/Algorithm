import numpy as np

def solution(arr1, arr2):
    answer = []
    
    for i in range(len(arr1)):
        answer.append([])
        for j in range(len(arr2[0])):
            params = 0
            for k in range(len(arr2)):
                params += arr1[i][k] * arr2[k][j]
            answer[i].append(params)
            

    return answer