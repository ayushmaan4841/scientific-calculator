import math 
def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    return x / y
def exponent(x, y):
    return x**y
def modulus(x, y):
    return x%y 
def log(x):
    return log(x)
def sin(x):
    return sin(x)
def cos(x):
    return cos(x)
def tan(x):
    return(x)              
print("Select operation.")
print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")
print("5.Exponent")
print("6.Modulus")
print("Scientfic")
print("7.Log")
print("8.sin")
print("9.cos")
print("10.tan")
while True:
    choice = input("Enter choice(1/2/3/4/5/6/7/8/9/10): ")
    if choice == '1':
        a= float(input("Enter first number: "))
        b= float(input("Enter second number: "))
        print(add(a, b))
    elif choice == '2':
        a= float(input("Enter first number: "))
        b= float(input("Enter second number: "))
        print(subtract(a, b))

    elif choice == '3':
        a= float(input("Enter first number: "))
        b= float(input("Enter second number: "))
        print(multiply(a, b))

    elif choice == '4':
        a= float(input("Enter first number: "))
        b= float(input("Enter second number: "))
        if (b==0):
            print("not possible")
        else:
            print(divide(a, b))
    elif choice == '5':
        a= float(input("Enter first number: "))
        b= float(input("Enter second number: "))
        print(exponent(a, b))     
    elif choice == '6':
        a= float(input("Enter first number: "))
        b= float(input("Enter second number: "))
        if (b==0):
            print("Invalid")
            print(modulus(a, b))
    elif choice == '7':
        a=float(input("Enter a number "))
        print((math.log10(a)))
    elif choice == '8':
        a=float(input("Enter a number"))
        print((math.sin(a)))
    elif choice == '9':
        a=float(input("Enter aa number"))
        print((math.cos(a)))
    elif choice == '10':
        a=float(input("Enter a number"))
        print((math.tan(a)))      
    another = input("Another Calculation? yes/no: ")
    if another == "no":
        break
    else:
        print("Invalid Input")
