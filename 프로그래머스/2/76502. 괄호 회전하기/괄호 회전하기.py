def check(s):
    stack = []
    
    for w in s :
        if w in ("(", "[", "{"):
            stack.append(w)
        else:
            if len(stack) == 0:
                return False
            
            sw = stack.pop()
            
            if (sw =="(" and w!=")") or (sw =="[" and w!="]") or (sw =="{" and w!="}") :
                return False           
    
    return True



def solution(s):
    
    cnt = 0
    
    if s.count("(")!=s.count(")") or s.count("[")!=s.count("]") or s.count("{")!=s.count("}"):
        return cnt
    
    
    for _ in range(len(s)):
        s = s[1:] + s[0] 
        if check(s):
            cnt+=1

    return cnt