x = int(input("Enter x: "))
y = int(input("Enter y: "))
z = int(input("Enter z: "))
if (x > y) and (x > z):
    print("x is largest!")
elif (y > z) and (y > x):
    print("y is largest!")
else: 
    print("z is largest!")
    