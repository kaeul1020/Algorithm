import math
def solution(n):
    a= math.sqrt(n)
    return (int(a)+1)**2 if a%1 == 0.0 else -1