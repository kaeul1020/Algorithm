from itertools import combinations
from collections import Counter

def solution(clothes):
    answer = 1
    counts = Counter()
    for cloth, cat in clothes:
        counts[cat] += 1
    
    for cnt in counts.values():
        answer *= (cnt + 1)
        
    return answer - 1