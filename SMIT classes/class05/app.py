# def temp_func():
#  y = 20
# print('Inside function:', y)
# temp_func()
# print(y) # This will cause an error, as y is not


# x = 10 # global variable
# def show_scope():
#  x = 5 # local variable
# print('Inside function:', x)
# show_scope()
# print('Outside function:', x)


# global
# x =10
# def my_fun():
#     # local fun
#     x = 30
#     print(x)
# # global call
# my_fun()
# print(x)

x =10
# def my_fun():
#    # call global veriable can change value
#    global x
#    x = 30
#    print(x)
# # global call
# my_fun()
# print(x)


# Total_student = 200
# def students():
#    present = int(input('enter present students  = : '))
#    absent = Total_student- present
#    print(f'Present = : {present}')
#    return print(f"absent students = : {absent}")
# students()
# print(f"Total Enrolled  Students : {Total_student}")

# def add(a, b):
#    return a * b
# result = add(3, 4)
# print('Sum:', result)

# import datetime
# now = datetime.datetime.now()
# print('Current date and time:', now)

x = 10
def fun():
 
    x = 5
    print('local',x)
fun()
print('global',x)