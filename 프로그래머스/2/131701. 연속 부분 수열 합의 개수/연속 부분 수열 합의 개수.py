def solution(elements):
    history = [0 for _ in range(len(elements)+1)]
    answer_set = set()
    
    for dist in range(len(elements)):
        for start in range(len(elements)):
            # print(f"start : {start}, dist : {dist}")
            end = (start+dist)%len(elements)
            history[start] += elements[end]
            # print(history)
            answer_set.add(history[start])
            # print(answer_set)
        # print("=========")
    
    return len(answer_set)