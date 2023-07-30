class Person:
    def __init__(self):
        self.name: str = "A"


mary = Person()
mary.name = 22
print(mary.name)

# Copy of the array to modify
my_list = [5, 76, 8, 5, 3, 3, 56, 5, 23]

# Loop from 0 up to the number of elements
# in the array:
for index in range(len(my_list)):
    # Modify the element by doubling it
    my_list[index] = my_list[index] * 2

# Print the result
print(my_list)

# Copy of the array to modify
my_list = [5, 76, 8, 5, 3, 3, 56, 5, 23]

# Loop through each element in myArray
for item in my_list:
    # This doubles item, but does not change the array
    # because item is a copy of a single element.
    item = item * 2

# Print the result
print(my_list)

#x = "This is a sample string"
x = "0123456789"

print("x=", x)


class Person:
    def __init__(self):
        self.name: str = "A"


mary = Person()
mary.name = 22
print(mary)

# Accessing the first character ("T")
print("x[0]=", x[0])

# Accessing the second character ("h")
print("x[1]=", x[1])

# Accessing from the right side ("g")
print("x[-1]=", x[-1])

# Access 0-5 ("This ")
print("x[:6]=", x[:6])
# Access 6 to the end ("is a sample string")
print("x[6:]=", x[6:])
# Access 6-8
print("x[6:9]=", x[6:9])