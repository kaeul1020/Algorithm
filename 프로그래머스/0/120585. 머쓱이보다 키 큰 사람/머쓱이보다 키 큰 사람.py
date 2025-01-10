def solution(array, height):
    array = sorted(array, reverse=True)
    for i, a in enumerate(array):
        if a <= height:
            return i
    return len(array)