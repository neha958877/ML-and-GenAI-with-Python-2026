print("First 10 natural numbers")
def print_natural_numbers():
    for i in range(1, 11):
        print(i)
print_natural_numbers()

print("Sum of first N natural numbers")
def sum_natural_numbers(n):
    return n * (n + 1) // 2
n = int(input("Enter N: "))
print("Sum =", sum_natural_numbers(n))

print("Reversing a number")
def reverse_number(num):
    rev = 0
    while num > 0:
        digit = num % 10
        rev = rev * 10 + digit
        num //= 10
    return rev
num = int(input("Enter a number: "))
print("Reverse =", reverse_number(num))

print("Count digits in a number")
def count_digits(num):
    count = 0
    while num > 0:
        count += 1
        num //= 10
    return count
num = int(input("Enter a number: "))
print("Number of digits =", count_digits(num))

print("Check a palindrome number")
def is_palindrome(num):
    original = num
    rev = 0
    while num > 0:
        digit = num % 10
        rev = rev * 10 + digit
        num //= 10
    return original == rev
num = int(input("Enter a number: "))
if is_palindrome(num):
    print("Palindrome Number")
else:
    print("Not a Palindrome Number")

print("Print fibonacci series")
def fibonacci(n):
    a = 0
    b = 1

    for i in range(n):
        print(a, end=" ")
        c = a + b
        a = b
        b = c

n = int(input("Enter number of terms: "))
fibonacci(n)

print("Calculator")
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = int(input("Enter your choice: "))

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if choice == 1:
    print("Result =", add(num1, num2))
elif choice == 2:
    print("Result =", subtract(num1, num2))
elif choice == 3:
    print("Result =", multiply(num1, num2))
elif choice == 4:
    if num2 != 0:
        print("Result =", divide(num1, num2))
    else:
        print("Division by zero not allowed")
else:
    print("Invalid Choice")


print("Create a Text File and Store Student Details")
file = open("student.txt", "w")

name = input("Enter student name: ")
roll = input("Enter roll number: ")
marks = input("Enter marks: ")

file.write("Name: " + name + "\n")
file.write("Roll Number: " + roll + "\n")
file.write("Marks: " + marks + "\n")

file.close()

print("Student details saved successfully.")


print("Read Data from a File")
file = open("student.txt", "r")

data = file.read()

print("File Contents:")
print(data)

file.close()


print("Handle Division by Zero Using Exception Handling")
try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    result = num1 / num2

    print("Result =", result)

except ZeroDivisionError:
    print("Cannot divide by zero!")

except ValueError:
    print("Please enter valid numbers.")


print("Create a Student Class with Name and Marks")
class Student:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print("Name:", self.name)
        print("Marks:", self.marks)


name = input("Enter student name: ")
marks = int(input("Enter marks: "))

s1 = Student(name, marks)

s1.display()