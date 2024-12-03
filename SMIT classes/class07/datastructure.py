numbers = [1, 3, 5, 7]

# Append an item, it will be add the item last in index

numbers.append(9)

print(numbers) # Output: [1, 3, 5, 7, 9]

numbers.extend([11, 13])

print(numbers) # Output: [1, 3, 5, 7, 9, 11, 13]

numbers.insert(0, "Manzoor")# 1st show index number and 2nd add itme

print(numbers) # Output: [1, 3, 4, 5, 7, 9, 11, 13]