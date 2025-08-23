N, R, C = map(int, input().split())

def vis(r,c, n):
    if n == 0:
        return 0
    
    half = 2**(n-1)
    for i in range(4):
       if r < half and c < half : return vis(r, c, n-1)
       elif r < half and c >= half : return half**2 + vis(r, c-half, n-1)
       elif r >= half and c < half : return half**2 *2 + vis(r-half, c, n-1)
       else : return half**2 *3 + vis(r-half, c-half, n-1)
        
print(vis(R, C, N))