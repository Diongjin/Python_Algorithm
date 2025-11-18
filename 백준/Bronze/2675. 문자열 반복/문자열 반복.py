testcase = int(input())

for _ in range(testcase):
    n,string = input().split()

    for idx in string:
        print(int(n)*idx,end="")

    print()