a,b = map(int, input().split())

#45분 일찍 알람

b -= 45

if b<0:
    a-=1
    b+=60
    if a<0:
        a= 23

print(a,b)