n = int(input())

number = list(map(int,input().split()))

cnt  = 0 # 소수 갯수

for i in number: #1, 3, 5, 7
    if i == 1:
        continue

    for j in range(2,i):
        if i%j == 0:
            break
    else:
        cnt+=1
print(cnt)

