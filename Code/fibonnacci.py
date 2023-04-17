steps = int(input("Enter no. of steps: "))
x = 0
y = 1
sum = 0
print("Fibonacci Series:")
count = 0
while count < steps:
    print(x)
    sum = x + y
    x = y
    y = sum
    count += 1