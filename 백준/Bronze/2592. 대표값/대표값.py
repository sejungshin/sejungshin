A = [int(input()) for i in range(10)]
print(sum(A)//10)
print(max(A, key=A.count))