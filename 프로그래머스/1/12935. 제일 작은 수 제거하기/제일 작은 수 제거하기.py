def solution(arr):
    min_arr = min(arr)
    arr.remove(min_arr)
    return [-1] if len(arr)==0 else arr