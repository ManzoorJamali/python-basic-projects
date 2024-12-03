


# def greet():
#    Total_student = 200
#    present = int(input('enter present students  = : '))
#    absent = Total_student- present
# #    print(f'Present = : {present}')
# #    print('total student')
#    return f"absent students = : {absent}"


total_sum = 0

def add_numbers(a, b):
    global total_sum  
    total_sum = a + b  
    return total_sum

# Test the function with some inputs
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

result = add_numbers(num1, num2)
print(f"The sum of {num1} and {num2} is: {result}")
print(f"The total_sum global variable is now: {total_sum}")
