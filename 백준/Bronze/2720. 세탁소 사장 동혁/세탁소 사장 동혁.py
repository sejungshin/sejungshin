t = int(input())
for i in range(t):
    number = int(input())

    quarter = number//25

    dime = number %25 //10

    nickel = number %25 %10 //5

    penny = number %25 %10 %5

    print(quarter, dime, nickel, penny)