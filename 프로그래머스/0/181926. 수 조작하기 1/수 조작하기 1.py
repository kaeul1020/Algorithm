def solution(n, control):
    dic = {'w':1, 's':-1, 'd':10, 'a':-10}
    for c in control:
        n += dic[c] 
    return n