rythem = list(map(int,input().split()))


if rythem == sorted(rythem):
    print("ascending")
elif rythem == sorted(rythem,reverse=True):
    print("descending")
else:
    print("mixed")