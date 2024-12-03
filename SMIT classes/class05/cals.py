# def calculator(num1, operation, num2):
#     if operation == "+":
#      return num1 + num2
    
#     elif operation =="-":
#        return num1 - num2
#     elif operation == "*":
#        return  num1 * num2
#     elif operation == "/":
#        if num2 != '0':
#         return num1 / num2
#        else:
#         return 'error '
#     else:
#       return "Error Invalid operation "
    

# num1 = int(input('enter num1 = : '))
# operation = input('enter operation')
# num2 = int(input('enter num2 =:'))
# calculat = calculator(num1,operation,num2)
# print(calculator)


# Simple Calculator in Python

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero is not allowed."
    return x / y

print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

while True:
    # Take input from the user
    choice = input("Enter choice (1/2/3/4): ")

    # Check if choice is one of the options
    if choice in ('1', '2', '3', '4'):
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == '1':
            print(f"The result is: {add(num1, num2)}")

        elif choice == '2':
            print(f"The result is: {subtract(num1, num2)}")

        elif choice == '3':
            print(f"The result is: {multiply(num1, num2)}")

        elif choice == '4':
            print(f"The result is: {divide(num1, num2)}")
    else:
        print("Invalid input. Please select a valid operation.")

    # Ask user if they want to perform another calculation
    next_calculation = input("Do you want to perform another calculation? (yes/no): ")
    if next_calculation.lower() != 'yes':
        break


