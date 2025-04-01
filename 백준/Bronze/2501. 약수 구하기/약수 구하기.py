N, K = map(int, input().split(' '))

count, result = 0, 0 

for n in range(1, N+1):
  if N % n == 0 :
    count +=1
    if count == K : 
      result = n
      break

if count < K :
  result = 0

print(result)