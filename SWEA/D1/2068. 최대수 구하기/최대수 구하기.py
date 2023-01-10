t = int(input())

for i in range(1, t + 1):
    
    li = map(int, input().split())
    print("#" + str(i), max(li))