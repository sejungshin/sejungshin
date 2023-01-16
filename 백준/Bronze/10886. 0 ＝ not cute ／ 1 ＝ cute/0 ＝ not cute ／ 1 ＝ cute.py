T = int(input()) 
sum = 0

for a in range(T):
    a = 0
    if int(input()) == 1:
        sum = sum + 1

if sum > T//2:
    print('Junhee is cute!')
else:
    print('Junhee is not cute!')