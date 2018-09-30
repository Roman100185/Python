___author___ = "Roman Puchkov"

# Task_1
num=int(input("Enter number from 1 to 10 "))
while num<=10:
	num+=2
	print(num)

# Task_2.1
num1=int(input("Enter first number "))
num2=int(input("Enter second number "))
num1,num2=num2,num1 #поменять местами переменные
print("First number is", num1)
print("Second number is", num2)

# Task_2.2
num1=int(input("Enter first number "))
num2=int(input("Enter second number "))
num1=num1+num2 #поменять местами переменные при помощи арифметических операций
num2=num1-num2
num1=num1-num2
print("First number is", num1)
print("Second number is", num2)

# Task_3
name=input("Enter your name ")
age=int(input("Enter your age "))
if age >= 18:
	print (name,", you can enter!")
	access = True
else:
	print (name,", sorry, but you have to leave this resource!")
	access = False
