num = int(input("Enter a number for factorial: "))
product = 1
for i in range(1, num + 1):
    product = product * i
    if num == 0:
        print(num, "factorial is: 1")
print(num, "factorial is:", product)





