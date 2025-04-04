peoples = [0]

for _ in range(10):
    minus, plus = map(int, input().split(' '))
    peoples.append(peoples[-1]-minus+plus)

print(max(peoples))