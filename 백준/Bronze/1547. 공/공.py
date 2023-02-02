ls = [1, 2, 3]
T = int(input())
for i in range(T):
    x, y = list(map(int, input().split()))
    index_x, index_y = ls.index(x), ls.index(y)
    ls[index_x], ls[index_y] = ls[index_y], ls[index_x]

print(ls[0])