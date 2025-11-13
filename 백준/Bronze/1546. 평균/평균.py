n = int(input())
score = list(map(int,input().split()))

m = max(score)

new_score=[]

for scores in score:
    new_score.append(scores/m*100)

avg = sum(new_score)/n

print(avg)