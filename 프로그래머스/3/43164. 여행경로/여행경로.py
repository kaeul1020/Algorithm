def solution(tickets):
    
    graph={}
    
    keys=set()
    for u, v in tickets:
        keys.add(u)
        keys.add(v)
        
    for key in keys:
        graph[key] = []
        
    for u, v in tickets:
        graph[u].append(v)
        
    for key in keys:
        graph[key] = sorted(graph[key])

    visited={}
    for key, value in graph.items():
        visited[key] = [False for _ in range(len(value))]
    
    def dfs(cur,stack):
        if len(stack) == len(tickets)+1:
            return stack

        for i, nxt in enumerate(graph[cur]):
            if visited[cur][i] == False:
                visited[cur][i] = True
                stack.append(nxt)
                # print(f"append : {nxt}")
                res = dfs(nxt, stack)
                if res : 
                    return res
                stack.pop()
                # print(f"pop : {nxt}")
                visited[cur][i] = False
    

    return dfs("ICN",["ICN"])