max_score = 0
max_result = -1

for i in range(5):
    score = list(map(int, input().split()))

    if sum(score) > max_result:
        max_result = sum(score)
        max_score = i+1

print(max_score, max_result)