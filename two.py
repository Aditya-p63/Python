# num = 10
# if num>0: 
#     print("positive number")
# elif num == 0:
#     print("zero")
# else :
#     print("negative number")
    
# age = 3
# if age > 18 :
#     if age < 30 :
#         print("adult")
#     else : 
#         print("ol
# d")


# fruits = ["apple", "banana", "cherry"];
# for item in fruits: 
#      print(item)
     
# for i in range(5):
#     print(i)
    
# count = 5
# while count > 0:
#     print(count)
#     if count == 3: break
#     count -= 1


# for i in range(10):
#     print(i)    
#     if i == 4:
#         continue


# num = int(input("Enter a number: "))
# if num > 1:
#     for i in range(2, num):
#         if (num % i) == 0:
#             print(num, "is not a prime number")
#             break
#     else:
#         print(num, "is a prime number")
# else:
#     print(num, "is not a prime number")
#
# def add(a, b):
#     return a + b
#
# def subtract(a, b):
#     return a - b
#
# def multiply(a, b):
#     return a * b
#
# def divide(a, b):
#     if b == 0:
#         raise ValueError("Cannot divide by zero")
#     return a / b
#
# while True:
#     print("\nmenu")
#     print("1. Addition")
#     print("2. Subtraction")
#     print("3. Multiplication")
#     print("4. Division")
#
#     choice = int(input("Enter your choice (1-4): "))
#
#     if(choice == 5):
#         print("Exiting the program.")
#         break
#     num1 = float(input("Enter first number: "))
#     num2 = float(input("Enter second number: "))
#     if choice == 1:
#         print("Result:", add(num1, num2))
#     elif choice == 2:
#         print("Result:", subtract(num1, num2))
#     elif choice == 3:
#         print("Result:", multiply(num1, num2))
#     elif choice == 4:
#         try:
#             print("Result:", divide(num1, num2))
#         except ValueError as e:
#             print(e)
#     else:
#         print("Invalid choice. Please try again.")
#

# def fact(n):
#     if n == 0 :
#         return 1
#     return n*fact(n-1)
# print(fact(5))

# def fact(n):
#     f = 1
#     for i in range (1,n+1):
#         f *=i
#     return f
#
# print (fact(5))


