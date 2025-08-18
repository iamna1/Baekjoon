n = int(input())
score = list(map(int, input().split()))
max_score = max(score)
print(max_score)
for i in range(n):
    score[i] = score[i] * 100 / max_score
print(sum(score)/ n)