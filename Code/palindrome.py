num = int(input("Enter a no.: "))
sum = 0
temp = num
while temp > 0:
    digit = temp % 10
    sum = sum * 10 + digit
    temp //= 10
if num == sum:
    print(num, "is palindrome.")
else:
    print(num, "is not palindrome.")