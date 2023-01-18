a = input()
alphabet = 'abcdefghijklmnopqrstuvwxyz'

for i in alphabet:
    if i in a:
        print(a.index(i), end= ' ')
    else:
        print(-1, end=' ')