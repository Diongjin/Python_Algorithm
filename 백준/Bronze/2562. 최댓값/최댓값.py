number = []

for i in range(9):
    n = int(input())
    number.append(n)

print(max(number))
print(number.index(max(number))+1)