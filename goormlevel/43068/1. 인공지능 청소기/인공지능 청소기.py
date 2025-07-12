# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean


T = int(input())

for _ in range(T):
	x, y, n  = map(int, input().split(" "))

	dist = abs(x-0) + abs(y-0)

	flag = "NO"

	if n >= dist and (n-dist)%2 == 0:
		flag = "YES"
	
	print(flag)
	