N = []

n,k = map(int, input().split())

for i in range(1,n+1):
    if n % i == 0:
        N.append(i)
    
if k > len(N):
    print(0)
else :
    print(N[k-1])