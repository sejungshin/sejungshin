numbers = []

for i in range(9):
    N = int(input())
    numbers.append(N)
    
print(max(numbers))
print(numbers.index(max(numbers))+1)