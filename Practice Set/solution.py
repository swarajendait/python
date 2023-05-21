# 1. Calculate the area of a rectangle
length = float(input("Enter the length: "))
width = float(input("Enter the width: "))
area = length * width
print("The area of the rectangle is:", area)

# 2. Check if a number is positive, negative, or zero
number = float(input("Enter a number: "))
if number > 0:
    print("Positive")
elif number < 0:
    print("Negative")
else:
    print("Zero")

# 3. Find the maximum of two numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
maximum = max(num1, num2)
print("The maximum number is:", maximum)

# 4. Check if a year is a leap year
year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap year")
else:
    print("Not a leap year")

# 5. Convert kilometers to miles
kilometers = float(input("Enter the distance in kilometers: "))
miles = kilometers * 0.621371
print("The distance in miles is:", miles)

# 6. Check if a string is a palindrome
string = input("Enter a string: ")
if string == string[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")

# 7. Find the sum of all numbers from 1 to n
n = int(input("Enter a number: "))
sum = 0
for i in range(1, n+1):
    sum += i
print("The sum is:", sum)

# 8. Print the multiplication table of a number
number = int(input("Enter a number: "))
for i in range(1, 11):
    print(number, "x", i, "=", number * i)

# 9. Calculate the average of three numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))
average = (num1 + num2 + num3) / 3
print("The average is:", average)

# 10. Find the square of a number
number = float(input("Enter a number: "))
square = number ** 2
print("The square is:", square)

# 11. Find the length of a string
string = input("Enter a string: ")
length = len(string)
print("The length of the string is:", length)

# 12. Check if a number is divisible by another number
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
if num1 % num2 == 0:
    print("Divisible")
else:
    print("Not divisible")

# 13. Find the sum of all even numbers between 1 and n
n = int(input("Enter a number: "))
sum = 0
for i in range(2, n+1, 2):
    sum += i
print("The sum of even numbers is:", sum)

# 14. Count the number of vowels in a string
string = input("Enter a string: ")
vowels = "aeiou"
count = 0
for char in string:
    if char.lower() in vowels:
        count += 1
print("The number of vowels is:", count)

# 15. Check if a number is a palindrome
number = int(input("Enter a number: "))
temp = number
reverse = 0
while temp > 0:
    digit = temp % 10
    reverse = reverse * 10 + digit
    temp //= 10
if number == reverse:
    print("Palindrome")
else:
    print("Not a palindrome")

# 16. Find the largest element in a list
numbers = [2, 5, 1, 8, 4]
maximum = max(numbers)
print("The largest element is:", maximum)

# 17. Remove duplicate elements from a list
numbers = [2, 5, 1, 2, 4, 5, 1, 2]
unique_numbers = list(set(numbers))
print("List after removing duplicates:", unique_numbers)

# 18. Check if a string is an anagram of another string
string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")
if sorted(string1) == sorted(string2):
    print("Anagram")
else:
    print("Not an anagram")

# 19. Sort a list of numbers in ascending order
numbers = [5, 2, 7, 1, 3]
numbers.sort()
print("List after sorting:", numbers)

# 20. Find the second largest element in a list
numbers = [5, 2, 7, 1, 3]
sorted_numbers = sorted(numbers)
second_largest = sorted_numbers[-2]
print("The second largest element is:", second_largest)

# 21. Count the number of words in a sentence
sentence = input("Enter a sentence: ")
words = sentence.split()
count = len(words)
print("The number of words is:", count)

# 22. Check if a number is a prime number
number = int(input("Enter a number: "))
if number > 1:
    for i in range(2, int(number/2)+1):
        if number % i == 0:
            print("Not a prime number")
            break
    else:
        print("Prime number")
else:
    print("Not a prime number")

# 23. Calculate the factorial of a number
number = int(input("Enter a number: "))
factorial = 1
for i in range(1, number+1):
    factorial *= i
print("The factorial is:", factorial)

# 24. Generate a random number between a given range
import random
start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))
random_number = random.randint(start, end)
print("The random number is:", random_number)

# 25. Check if a string is a palindrome using a function
def is_palindrome(string):
    return string == string[::-1]

string = input("Enter a string: ")
if is_palindrome(string):
    print("Palindrome")
else:
    print("Not a palindrome")

# 26. Find the sum of the digits of a number using a function
def sum_of_digits(number):
    sum = 0
    while number > 0:
        digit = number % 10
        sum += digit
        number //= 10
    return sum

number = int(input("Enter a number: "))
sum = sum_of_digits(number)
print("The sum of digits is:", sum)

# 27. Calculate the area of a circle
import math
radius = float(input("Enter the radius: "))
area = math.pi * radius ** 2
print("The area of the circle is:", area)

# 28. Find the average of a list of numbers
numbers = [5, 2, 7, 1, 3]
average = sum(numbers) / len(numbers)
print("The average is:", average)

# 29. Check if a number is a perfect square
number = int(input("Enter a number: "))
if number > 0:
    if math.isqrt(number) ** 2 == number:
        print("Perfect square")
    else:
        print("Not a perfect square")
else:
    print("Not a perfect square")

# 30. Check if a string is a pangram (contains all the letters of the alphabet)
def is_pangram(string):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    return all(letter in string.lower() for letter in alphabet)

string = input("Enter a string: ")
if is_pangram(string):
    print("Pangram")
else:
    print("Not a pangram")
