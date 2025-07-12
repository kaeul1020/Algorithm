# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

n, m = map(int, input().split(" "))

salt = int(n*7/100)
total = int(n + m)


print(f"{(int(10000*salt/total)/100):.2f}")