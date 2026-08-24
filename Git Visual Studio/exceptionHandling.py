# try:
#     print("It is outer Try")
    
#     try:
#         num=int(input("Enter the number "))
#         print(10/num)
#     except ZeroDivisionError:
#         print("Inner: Divide by zero Error")
# except:
#     print("Outer Exception")

# try:
#     age=int(input("Enter your age "))
#     print(age)
# except:
#     print("Invalid number")
# else:
#     print("No error Occured")
# finally:
#     print("Completed")


try:
    print("Age should not be less then 18")
    age>=18


except ZeroDivisionError:
        print("Inner: Age cannot be zero")

else:
        print("Age is equal 18 ")

