num = int(input("Enter a no.: "))
f = 0
if num > 1:
    for i in range(2, num):
        if(num % i == 0):
            f = 1
if f == 1:
    print(num, "is not prime!")
else:
    print(num, "is prime!")