def add(x,y):
    return(x+y)

def subtract(x,y):
    return(x-y)


print("Adding And Subtracting Calculator")
print("1. Add")
print("2. Subtract")

choice = input("Enter choice 1 or 2. ")

if choice in ('1','2'):
    num1 = float(input("Enter first number "))
    num2 = float(input("Enter second number "))

if choice == '1':
    print("Result:", add(num1, num2))
else:
    print("Results:", subtract(num1, num2))
