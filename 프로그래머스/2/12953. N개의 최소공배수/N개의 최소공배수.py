from collections import Counter

def solution(arr):
    result_dict = Counter()
    for a in arr:
        cnt = Counter()
        
        i, x = 2, a
        while i <= x:
            while x%i ==0 :
                cnt[i] += 1
                x //= i
            result_dict[i] = max(result_dict[i], cnt[i])
            i += 1

    result = 1
    for k, v in result_dict.items():
        result *= k**v
            
    return result