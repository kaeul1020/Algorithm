def solution(price):
    answer = price
    if price>=500000:
        answer = price*80/100
    elif price >= 300000:
        answer = price*90/100
    elif price >= 100000:
        answer = price*95/100
    return int(answer)