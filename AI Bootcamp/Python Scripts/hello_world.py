scores = [92, 87, 68, 75, 96]

# Return the max (or highest value) item in a list
max = max(scores)
print(max)

# Return the min (or lowest) item in a list
min = min(scores)
print(min)
# Return the sum of the items in a list
total = sum(scores)
print(total)
# Return the length of the list
length = len(scores)
print(length)
# Use sum and len to calculate average
average = total/length
print(average)

# Create a tuple, a sequence of immutable Python objects that cannot be changed
my_tuple = ("a", 25, "Chester Bennington")
print(type(my_tuple))

# Information functions also work on tuples, provided they contain valid data
# types