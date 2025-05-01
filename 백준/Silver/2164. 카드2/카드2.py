from collections import deque

N = int(input())
cards = deque([i for i in range(1, N+1)])
last_card = 0
while True:
    last_card = cards.popleft()
    if len(cards) == 0:
        break
    cards.append(cards.popleft())
print(last_card)