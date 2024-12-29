def solution(s):
    s = s.lower()
    return False if s.count('y') != s.count('p') else True