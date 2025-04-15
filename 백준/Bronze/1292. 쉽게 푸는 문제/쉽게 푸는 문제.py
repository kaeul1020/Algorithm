a, b = map(int, input().split(' '))

pers = []

for i in range(1, b+1):
    for j in range(i):
        pers.append(i)
        
print(sum(pers[a-1:b]))