import math

def area_circle(radius):
    return math.pi * radius ** 2

def area_rectangle(length, width):
    return length * width

def area_triangle(base, height):
    return 0.5 * base * height

def main():
    print("Choose a shape to calculate its area:")
    print("1. Circle")
    print("2. Rectangle")
    print("3. Triangle")
    
    choice = input("Enter the number corresponding to your choice: ")
    
    if choice == '1':
        radius = float(input("Enter the radius of the circle: "))
        print("Area of the circle:", area_circle(radius))
    
    elif choice == '2':
        length = float(input("Enter the length of the rectangle: "))
        width = float(input("Enter the width of the rectangle: "))
        print("Area of the rectangle:", area_rectangle(length, width))
    
    elif choice == '3':
        base = float(input("Enter the base of the triangle: "))
        height = float(input("Enter the height of the triangle: "))
        print("Area of the triangle:", area_triangle(base, height))
    
    else:
        print("Invalid choice. Please try again.")

# Run the main function
main()
