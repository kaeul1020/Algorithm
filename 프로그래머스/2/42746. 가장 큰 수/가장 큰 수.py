def solution(numbers):
    
    numbers = list(map(str, numbers))
    
    max_len = max(len(n) for n in numbers )

    numbers.sort(key=lambda x : x * max_len, reverse=True)
    
    answer = ''.join(numbers)
    
    if answer[0] == '0':
        return '0'
    
    return answer