N = int(input())

tiles = [1,2]
for idx in range(2, N):
    tiles.append((tiles[idx-1] + tiles[idx-2])%10007)

print(tiles[N-1])