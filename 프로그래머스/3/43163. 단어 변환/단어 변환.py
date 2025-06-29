from collections import deque

def solution(begin, target, words):
    
    if not target in words:
        return 0
    
    if not begin in words:
        words.append(begin)
    
    graph = {}
    for word in words:
        graph[word] = []
        for i in range(len(word)):
            for comp_word in words:
                if word == comp_word :
                    continue
                if word[:i] == comp_word[:i] and word[i+1:] == comp_word[i+1:]:
                    graph[word].append(comp_word)
    
    dist = { w : 0 for w in words}

    q = deque([begin])
    dist[begin] = 1
    
    while q:
        cur = q.popleft()

        for nxt in graph[cur]:
            if dist[nxt] == 0 :
                q.append(nxt)
                dist[nxt] = dist[cur]+1

    return dist[target]-1