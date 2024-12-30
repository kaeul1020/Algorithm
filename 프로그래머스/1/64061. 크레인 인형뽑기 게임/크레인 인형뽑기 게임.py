def solution(board, moves):
    answer, n = 0, len(board)
    stacks, basket = [], []
    
    # 재정렬
    for i in range(n):
        stacks.append([])
        for j in range(n):
            if board[j][i] != 0 :
                stacks[i].insert(0, board[j][i])
    
    # 옮기기
    for i, m in enumerate(moves):
        try : 
            basket.append(stacks[m-1].pop())        
        except :
            continue

        while len(basket) >= 2 and (basket[-2] == basket[-1]) : 
            answer += 2
            basket.pop()
            basket.pop()

    return answer