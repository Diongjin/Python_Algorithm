X=[]
Y=[]

test = int(input())

for _ in range(test):
    x,y = map(int,input().split())
    X.append(x)
    Y.append(y)

for i in range(3):
    maxa = max(X)
    mina = min(X)
    maxb = max(Y)
    minb = min(Y)
    

print((maxa-mina)*(maxb-minb))