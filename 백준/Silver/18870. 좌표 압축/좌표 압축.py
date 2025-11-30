N = int(input())

x_list = list(map(int, input().split()))

x_unique_list = list(set(x_list))
x_unique_list.sort()

x_prime_dic = {}
for i, x in enumerate(x_unique_list):
    x_prime_dic[x] = i

answer = []
for x in x_list:
    answer.append(x_prime_dic[x])

print(*answer)