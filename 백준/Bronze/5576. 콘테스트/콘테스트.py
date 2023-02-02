for _ in range(2):
    a = []
    for _ in range(10):
        a.append(int(input()))
    print(sum(sorted(a)[-3:]))