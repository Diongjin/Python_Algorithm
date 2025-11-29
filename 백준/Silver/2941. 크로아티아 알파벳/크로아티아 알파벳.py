alpha = ['c=','c-','dz=','d-','lj','nj','s=','z=']

line = input()

for i in alpha:
    line = line.replace(i,'r')
print(len(line))