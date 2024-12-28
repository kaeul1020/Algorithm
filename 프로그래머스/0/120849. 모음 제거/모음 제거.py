def solution(my_string):
    answer=my_string
    for v in ['a', 'e', 'i', 'o', 'u']:
        answer = answer.replace(v,'')
    return answer