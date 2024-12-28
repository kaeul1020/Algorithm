import math
def solution(num_list):
    answer = 0
    if len(num_list) > 10:
        answer = sum(num_list)
    else :
        answer = math.prod(num_list)
    return answer