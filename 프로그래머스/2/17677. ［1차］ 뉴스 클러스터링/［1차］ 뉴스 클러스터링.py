def solution(str1, str2):
    
    str1, str2 = str1.upper(), str2.upper()
    
    # 두글자씩 str1, str2 끊기 -> 중복 허용
    str1s, str2s = [], []
    
    for i in range(len(str1)-1):
        if "A" <= str1[i] <= "Z" and "A" <= str1[i+1] <= "Z":
            str1s.append(f"{str1[i]}{str1[i+1]}")
    for i in range(len(str2)-1):
        if "A" <= str2[i] <= "Z" and "A" <= str2[i+1] <= "Z":
            str2s.append(f"{str2[i]}{str2[i+1]}")
            
            
    print(str1s, str2s)
    
    # str1, str2 교집합 구하기
    intersect = 0
    check = [False for _ in range(len(str2s))]
    for s1 in str1s:
        for i, s2 in enumerate(str2s) :
            if s1 == s2 and check[i] == False:
                intersect += 1
                check[i] = True
                
                break
    print(intersect)
    
    print((len(str1s)+len(str2s)-intersect))
    
    # 나눠
    if (len(str1s)+len(str2s)-intersect) == 0:
        return 65536
    else : 
        return int(intersect / (len(str1s)+len(str2s)-intersect) * 65536)
