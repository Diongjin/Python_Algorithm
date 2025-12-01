N = []

a = int(input())
b = int(input())


for i in range(a,b+1):
    if i == 1:
        continue
    for j in range(2,i):
        if i % j ==0:
            break
    else:
        N.append(i)

if not N:
    print(-1)
else:
    print(sum(N))
    print(min(N))