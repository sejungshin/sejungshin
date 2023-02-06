people = []
people_result = 0

for _ in range(4):
    a, b = map(int,input().split())
    people_result += b
    people_result -= a
    people.append(people_result)

print(max(people))