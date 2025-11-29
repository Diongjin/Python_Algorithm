string = input()

line = 'abcdefghijklmnopqrstuvwxyz'

for i in line:
    if i in string:
        print(string.index(i), end=" ")
    else :
        print("-1",end=" ")