alphabet = {'ABC':3,'DEF':4,'GHI': 5,'JKL':6,'MNO':7,'PQRS':8,'TUV':9,'WXYZ':10}
dial = input()
time = 0

for i in range(len(dial)):
    for a in alphabet.keys():
        if dial[i] in a:
            time += alphabet[a]
print(time)