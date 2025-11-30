test = int(input())

for _ in range(test):
    n = int(input())
    
    for i in [25,10,5,1]:
        print(n//i, end = " ")
        n %=i
    
    