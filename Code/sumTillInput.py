# Sum of first ()input natural numbers
num = int(input("Enter a no. to get the sum of the natural numbers till what you have entered: "))
sum = 0
for i in range(1, (num + 1)):
    sum += i
print("Sum is: ", sum)