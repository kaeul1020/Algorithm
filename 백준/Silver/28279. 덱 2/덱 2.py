from collections import deque
import sys

N = int(input())
deck = deque([])
for _ in range(N):
    order = list(map(int,sys.stdin.readline().split()))

    try : 
        if order[0] == 1 :
            deck.appendleft(order[1])
        elif order[0] == 2:
            deck.append(order[1])
        elif order[0] == 3 :
            print(deck.popleft())
        elif order[0] == 4:
            print(deck.pop())
        elif order[0] == 5:
            print(len(deck))
        elif order[0] == 6:
            print(int(len(deck)==0))
        elif order[0] == 7:
            print(deck[0])
        elif order[0] == 8:
            print(deck[-1])
    except : print(-1)
