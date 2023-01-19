a = int(input())
b = int(input())
c = int(input())

multi = a * b * c
multi_str = str(multi)

for i in range(10):
    print(multi_str.count(str(i)))
