n,m = map(int,input().split())

bucket = list(range(1,n+1))

for _ in range (m):
    i,j = map(int, input().split())

    bucket[i-1:j] = reversed(bucket[i-1:j])

for index in bucket:
    print(index,end = " ")