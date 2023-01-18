# 2789 유학 금지
word = input()
result = ''
for i in word:
    if i not in 'CAMBRIDGE':
        result = result + i
print(result)