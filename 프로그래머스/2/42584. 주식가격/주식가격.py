def solution(prices):
    answer = [ 0 for _ in range(len(prices))]
    stack = []
    
    for i, p in enumerate(prices):

        while stack != [] and stack[-1] > (p, i):
            sp, si = stack.pop()
            answer[si] = i-si

        stack.append((p,i))
        
        if i == len(prices)-1:
            while stack != []:
                sp, si = stack.pop()
                answer[si] = i-si

    return answer