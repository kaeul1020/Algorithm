A, B, C = map(int, input().split())

def slot(b):
    
    if b == 1:
        return A%C
    
    answer = slot(b//2)
    answer = answer*answer % C
        
    if b % 2 == 0:
        return answer
    else :
        return answer * A % C

print(slot(B) % C)