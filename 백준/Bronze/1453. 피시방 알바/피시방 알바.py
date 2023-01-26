t = int(input())
N = list(map(int, input().split()))
seat = []
cnt = 0

for i in range(t):
    if N[i] in seat:
        cnt += 1
    else:
        seat.append(N[i])
print(cnt)