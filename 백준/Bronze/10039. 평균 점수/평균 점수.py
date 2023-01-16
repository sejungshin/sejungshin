sum = 0
for a in range(5):
    score = int(input())
    if score >= 40:
        sum = sum+score
    else:
        sum = sum+40
print(int(sum / 5))