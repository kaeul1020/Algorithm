N = int(input())

users=[]

for i in range(N):
    age, name = input().split()
    users.append((i, int(age), name))
    
users.sort(key=lambda x : (x[1], x[0]))

for _, age, name in users:
    print(age, name)