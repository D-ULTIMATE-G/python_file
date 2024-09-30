# SIMPLE calculator

# calculator must be a function

#this is a basic calculator

# ask for first and second number
# print("")
# print("1, addition")
# operation = input("choose the operation  would")
# if operation = "1" 1

print("this is a simple calculator")

def calc():
    """ this is a basic calculator"""
    print("this is a simple calculator")
    print("enter your num1")
    num1 = int(input())
    print("enter your num2")
    num2 = int(input())
    print("choose your operator")
    print("1.add")
    print("2.subtract")
    print("3.multiply")
    print("4.divide")
    operation = input("choose one operator")
    if operation == "1" : 
        result = num1 + num2
        print(result)

    elif operation == "2" : 
        result = num2 - num1
        print(result)  

    elif operation == "3" : 
       result = num1 * num2
       print(result)
    elif operation == "4" : 
        try:
            result = num1 / num2
           
        except ZeroDivisionError:
            print("error: It is no allowed to divide by zero")
    else:
       print("invalid operation")
    again = input("do uu want to perform another operation").lower()

    if again == "yes":

     calc()
    else:
        print("goodbye")

calc()
 