def solution(n):
    a = list(map(int, str(n)))
    a.sort(reverse = True)
    return int(''.join(list(map(str, a))))