a,b = map(int, input().split())
c= int(input())
#c는 필요시간

if b+c <60:
    b+=c
else:
    a+=(b+c)//60
    b=(b+c)%60
    if a>=24:
        a=a%24 
print(a,b)