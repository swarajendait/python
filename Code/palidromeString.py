# To check if string is a palindrome
strInput = input("Enter string to see if it is palindrome or not: ")
strInput = strInput.casefold()
rev = ''.join(reversed(strInput))
if strInput == rev:
    print(strInput, "is a palindrome! Palindrome Version:", rev)
else:
    print(strInput, "is not a palindrome!")

#Alternative for num palindrome
num = int(input("Enter no.: "))
strify = str(num)
rev = ''.join(reversed(strify))
if strify == rev:
    print(num, "is palindrome! Palindrome: ", rev)
else:
    print(num, "is not palindrome!")
