# For the exercise, look up the methods and functions that are available for use
# with Python lists.

x = [1, 2, 3]
y = [8, 9, 10]

# self-note: lists is a collection of data- ordered and changeable

# For the following, DO NOT USE AN ASSIGNMENT (=).

# Change x so that it is [1, 2, 3, 4]
# YOUR CODE HERE

#adds single element arg to end of list
x.append(4)
print(x)

# Using y, change x so that it is [1, 2, 3, 4, 8, 9, 10]
# YOUR CODE HERE

#extends list by adding all items of a list passed as args to end
x.extend(y)
print(x)

# Change x so that it is [1, 2, 3, 4, 9, 10]
# YOUR CODE HERE

#removes item by index
del x[4]
print(x)

# Change x so that it is [1, 2, 3, 4, 9, 99, 10]
# YOUR CODE HERE

#appends all items by index
x.insert(-1,99)
print(x)

# Print the length of list x
# YOUR CODE HERE

#gets length of list
print(len(x))
# Print all the values in x multiplied by 1000
# YOUR CODE HERE

#for loop over x list
for i in x:
    print(i * 1000)