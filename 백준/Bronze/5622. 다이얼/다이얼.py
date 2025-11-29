alphabet = ['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']

word = input()
time = 0

for alpha in alphabet:
    for i in alpha:
        for j in word:
            if i==j:
                time += alphabet.index(alpha)+3
print (time)