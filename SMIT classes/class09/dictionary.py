

# person = {"name": "Alice", "age": 25, "city": "New York"}

# # # Accessing values
# # print(person["name"])  # Output: Alice
# # print(person["age"])   # Output: 25

# # Using .get() method (avoids KeyError if key doesn't exist)
# print(person.get("city"))       # Output: New York
# print(person.get("name"))    # Output: None


# # Using del
# del person["city"]

# # Using pop (also returns the removed value)
# removed_value = person.pop('age')
# print(removed_value)  # Output: 26

# Create a dictionary

student_grades = {"Alice": 85, "Bob": 90, "Charlie": 88}

# Get a value with get()

# grade = student_grades.get("Alice")

# print(grade) # Output: 85

# Get keys and values

# keys = student_grades.keys()

# values = student_grades.values()

# print(keys) # Output: dict_keys(['Alice', 'Bob', 'Charlie'])

# print(values) # Output: dict_values([85, 90, 88])

# # Update dictionary with new values

student_grades.update({"Alice": 95, "David": 92})

print(student_grades) # Output: {'Alice': 95, 'Bob': 90, 'Charlie': 88, 'David': 92}

# # Remove and return a value using pop()

removed_grade = student_grades.pop("Bob")
removed_grade = student_grades.pop("Alice")

print(removed_grade) # Output: 90

# # Clear all items from dictionary

# student_grades.clear()

# print(student_grades) # Output: {}




# student_grades = {"Alice": 85, "Bob": 90, "Charlie": 88}
# for key in list(student_grades.keys()):
#     if key in ("Bob","Alice"):
#         student_grades.pop(key)
# print(student_grades)


# for key, value in student_grades.items():
#     print(f'Key {key} value {value} ')


# # Traversing Keys

# person = {
#     "name": "Manzoor",
#     "age": 32,
#     "city": "Karachi"
# }
# print(person.get("name")) 

# for key, value in person.items():
#     print(f"{key}: {value}")

# person.pop('city')

# print(person)

# for key in person:
#     print(key)

# # Traversing Values
# for value in person.values():
#     print(value)

# Traversing Key-Value Pairs

