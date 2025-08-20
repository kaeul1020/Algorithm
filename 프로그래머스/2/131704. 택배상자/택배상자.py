from collections import deque

def solution(order):
    answer = 0
    order = deque(order) # order = FIFO : queue
    
    main = deque([ i for i in range(1, len(order)+1)])
    sub = [] # sub 컨테이너벨트 = FILO : stack
    rm_box = -1
    while order:
        cur_order = order.popleft()
#         print("==================")
#         print(cur_order, main, sub, answer)
        
        while len(main) + len(sub) > 0:
            
            # sub에서 꺼내올지, main에서 꺼내올지 정해야함.
            if len(main) != 0 and main[0] == cur_order:
                rm_box = main.popleft()
                answer += 1
                break
            elif len(sub) !=0 and sub[-1] == cur_order:
                rm_box = sub.pop()
                answer += 1
                break
            if len(main) != 0  :
                sub.append(main.popleft())
        
            if cur_order < rm_box:
                break
                
#             print(cur_order, main, sub, answer)
            
        if cur_order < rm_box:
            break

    return answer