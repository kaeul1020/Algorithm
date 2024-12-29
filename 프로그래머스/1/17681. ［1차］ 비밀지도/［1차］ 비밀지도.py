def solution(n, arr1, arr2):
    answer = [""]*n
    for i in range(n):
        arr1[i] = '0'*(n-len(bin(arr1[i])[2:]))+bin(arr1[i])[2:]
        arr2[i] = '0'*(n-len(bin(arr2[i])[2:]))+bin(arr2[i])[2:]
    
    for i in range(n):
        for j in range(n):
            if int(arr1[i][j]) + int(arr2[i][j]) != 0:
                answer[i]+= "#"
            else : 
                answer[i] += " "

    return answer