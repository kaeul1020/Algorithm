def solution(strArr):
    for i, s in enumerate(strArr):
        if i%2==1:
            strArr[i] = strArr[i].upper()
        else :
            strArr[i] = strArr[i].lower()
    return strArr