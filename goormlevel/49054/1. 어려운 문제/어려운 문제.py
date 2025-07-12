# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
N = int(input())


result = 1
for i in range(1,N+1):
	result *= i


if N > 3 : 
	while result >= 10:
		result = sum(list(map(int, str(result))))
print(result)
# while result//10 > 0:

	
	