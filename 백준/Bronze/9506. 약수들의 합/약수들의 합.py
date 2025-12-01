while(1):
    n = int(input())
    if n == -1:
        break

    N = []
    
    for i in range(1,n):
        if n% i == 0:
            N.append(i)
    
    if sum(N) != n:
        print(n,"is NOT perfect.")
    else:
        print(n,"= ",end="")
        for i in range(len(N)):
            if i!= len(N)-1:
                print(N[i],"+ ",end="")
            else:
                print(N[i])
    