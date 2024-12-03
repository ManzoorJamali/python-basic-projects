


def miles_to_km(miles):
    # 1 mile is approximately 1.60934 kilometers
    return miles / 1.60934

# Get user input
mile_value = float(input("Enter the number of miles: "))

# Call the function and display the result
kilometers = miles_to_km(mile_value)
print(f"{mile_value} miles is equal to {kilometers} kilometers.")

# another example
def add(a,b):
    return a+b
result = add(3,4)
print('sum : ', result)


# scops