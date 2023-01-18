word = input()
def solution(word):
    if word == word[::-1]:
        return 1
    else:
        return 0
print(solution(word))