
n = int(input()) 
a_list = list(map(int, input().split(" ")))
b_list = list(map(int, input().split(" ")))
k = int(input())

def count_up(i):
	b_list[i] = 0

	if i-1 < 0 :
		return 0
		
	b_list[i-1] += 1

	# print(f"count_up(i), i : {i}, b_list : {b_list}")

	if b_list[i-1] > a_list[i-1]:
		count_up(i-1)

	return 0
	

for _ in range(k):
	b_list[n-1] += 1
	if b_list[n-1] > a_list[n-1]:
		count_up(n-1)

for b in b_list:
	print(b, end="")
		
	