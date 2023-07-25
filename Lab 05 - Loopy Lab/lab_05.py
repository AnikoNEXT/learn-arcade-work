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