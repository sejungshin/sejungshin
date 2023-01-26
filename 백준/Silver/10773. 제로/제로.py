t = int(input())
ls = []

for i in range(t):
    number = int(input())

    if number == 0:
        ls.pop()
    else:
        ls.append(number)

result = sum(ls)
print(result)