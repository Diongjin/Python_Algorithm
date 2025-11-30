a= []


for i in range(9):
    a.append(list(map(int,input().split())))
    
max =-1
row =0
col = 0

for i in range(9):
    for j in range(9):
        if max < a[i][j]:
            max = a[i][j]
            row = i+1
            col = j+1
            
            
print(max)
print(row, col)