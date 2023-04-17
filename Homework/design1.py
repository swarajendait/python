# 1
# 2 2
# 3 3 3

#CODE:

num = int(input("Enter no. rows: "))

for i in range(num):
    for j in range(i+1):
        print(i+1, end=" ")
    print("\n")