A, B = map(int,input().split())
C = int(input())
A1 = A+C // 60
B1 = B+C % 60

if B1 >= 60:
  A1 += 1
  B1 -= 60

if A1 >= 24:
    A1 -= 24

print(A1, B1)