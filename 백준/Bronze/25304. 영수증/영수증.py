total = int(input())
testcase = int(input())

sum = 0

for i in range (0,testcase):
    price, count = map(int, input().split())

    sum += price*count


if(total == sum):
        print("Yes")
else:
        print("No")
