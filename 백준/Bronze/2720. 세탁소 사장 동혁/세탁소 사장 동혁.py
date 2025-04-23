coins = [25, 10, 5, 1]

T = int(input())

for t in range(T):
    C = int(input())
    for coin in coins:
        print(C//coin, end=" ")
        C = C%coin
    print('')