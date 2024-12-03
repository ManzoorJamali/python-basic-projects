# number =[0,1,2,3,4,5,6,7] 
# even_numbers = [x for x in number if x %2 ==0 ]
# print(even_numbers)

# #un given list
# a = [x for x in range(10) if x %2 == 0]
# print(a)

numbers = [1, 2, 3, 4]
# result = [x**2 if x % 2 == 0 else x**3 for x in numbers]
# print(result)  # Output: [1, 4, 27, 16]

# numbers = [1, 2, 3, 4]
# result = [x*2 if x % 2 == 0 else x*3 for x in numbers]
# print(result)  # Output: [1, 4, 27, 16]


new_list = []
for x in numbers:
    new_list.append(x)
    print(new_list)

# list = "12345"
# for x in list:
#     if x =='3':
#         print(f'Found {x}') 


# #string manipulation 
# name  = 'Manzoor'
# print(name.upper())
# print(name.lower())
# print(name.replace('Manzoor','jamali'))
# print(name.split(','))


    

my = []
for i in numbers:
  my.append(i)
  print(my)
