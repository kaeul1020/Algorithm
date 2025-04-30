while True:
    string = list(input())
    if len(string) == 1 and string[0] == ".":
        break
    
    stack, result = [], "yes"
    for s in string:
        if s in ['(', '[']:
            stack.append(s)
        elif s == ')':
            if len(stack)==0 or stack.pop() != '(': 
                result = "no"
                break
        elif s == ']':
            if len(stack)==0 or stack.pop() != '[': 
                result = "no"
                break
    
    if len(stack) != 0 : result = "no"
                
    print(result)