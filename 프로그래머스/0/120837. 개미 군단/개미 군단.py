def solution(hp):
    answer = 0
    damage = [5,3,1]
    
    for d in damage:
        answer += hp//d
        hp = hp%d
    
    return answer