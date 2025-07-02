def solution(n):
    count = 0
    for i in range(1, n+1):
        sum_num = 0
        for num in list(range(i,i+(n//i)+1)):
            sum_num += num
            
            # print(f"i : {i}, num : {num}, sum_num : {sum_num}, count : {count}")
            
            if sum_num > n:
                break
            elif sum_num == n:
                count+=1
                break
                
    return count