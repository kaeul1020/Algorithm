def solution(s):    
    stack = []
    
    for i in s:
        if i == "(":
            stack.append(i)
        else : 
            if len(stack) ==0:
                return False
            else:
                stack.pop(-1)
    
    if len(stack) == 0:
        return True
    else :
        return False
