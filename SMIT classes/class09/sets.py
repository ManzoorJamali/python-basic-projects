# # Create a set

# fruits = {"apple", "banana", "cherry"}

# # Add an item to the set

# fruits.add("orange")

# print(fruits) # Output: {'banana', 'orange', 'apple', 'cherry'}

# # Remove an item if it exists

# fruits.discard("banana")

# print(fruits) # Output: {'orange', 'apple', 'cherry'}

# # Union of two sets

# tropical_fruits = {"mango", "pineapple"}

# all_fruits = fruits.union(tropical_fruits)

# print(all_fruits) # Output: {'orange', 'apple', 'cherry', 'mango', 'pineapple'}

# # Intersection of sets

# berries = {"strawberry", "blueberry", "cherry"}

# common_fruits = fruits.intersection(berries)#use for common value

# print(common_fruits) # Output: {'cherry'}


present  = {f'present = Manzoor','ayaz','jamali'}

present.add( 'Mubeen')

print(f'Join the new student : {present}')

present.discard('Manzoor')
print(f'Leave : {present}')
# Unino Sets

absent = {'kamran', 'Arslan'}
all = present.union(absent)
print(f'All students {all}')
# Intersection of sets
late_students = {'zohaib','latif','ayaz'}
now_status   = present.intersection(late_students)
print(f'now the students are here {now_status}') 



# Task 1: Lists
numbers = [1, 2, 3, 4, 5, 6]
print('filter_even_numbers'(numbers))  # [2, 4, 6]
print('add_to_list'(numbers, 7))       # [1, 2, 3, 4, 5, 6, 7]

# Task 2: Tuples
tpl1 = (1, 2, 3)
tpl2 = (4, 5, 6)
print('unpack_tuple'(tpl1))            # (1, 2, 3)
print('combine_tuples'(tpl1, tpl2))    # (1, 2, 3, 4, 5, 6)

# Task 3: Dictionaries
my_dict = {'a': 1, 'b': 2}
print('add_key_value'(my_dict, 'c', 3)) # {'a': 1, 'b': 2, 'c': 3}
print('find_value'(my_dict, 'b'))       # 2
print('find_value'(my_dict, 'z'))       # Key not found

# Task 4: Sets
set1 = {1, 2, 3}
set2 = {3, 4, 5}
print('set_operations'(set1, set2))     # ({1, 2, 3, 4, 5}, {3}, {1, 2})
print('check_membership'(set1, 2))      # True
print('check_membership'(set1, 6))      # False 

