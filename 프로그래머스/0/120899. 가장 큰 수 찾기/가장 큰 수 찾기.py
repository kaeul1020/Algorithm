def solution(array):
    answer = [0,0]
    for i, a in enumerate(array):
        if a > answer[0]:
            answer = [a, i]
    return answer