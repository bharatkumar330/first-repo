# Create a variable and set it as a list
my_list = ["Bharat", "Aidan", "Miles", "Percy", "Tommy", "Janrey"]

# Methods for accessing parts of a list
last_element = my_list.pop()

# Return the value of a list at a given index
print(my_list[3])

# Return the index of the first object with a matching value
index = my_list.index("Aidan")
print(index)

# Return a list slice [index_start:index_end]
print (my_list[0:3])

# Methods for modifying a list

# Add an element onto the end of a list
my_list.append("Carla")
print(my_list)
# Change a specified element within a list at the given index
my_list[3] = "Arya"
print(my_list)
# Remove a specified object from a list
my_list.remove("Miles")
print(my_list)
# Remove the object at the index specified
del my_list[-1]
print(my_list)