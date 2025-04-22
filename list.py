# Create an empty list
numbers_list = []

# Append elements to numbers_list
numbers_list.append(10)
numbers_list.append(20)
numbers_list.append(30)
numbers_list.append(40)

# Insert the value 15 at the second position
numbers_list.insert(1, 15)

# Extend numbers_list with another list
numbers_list.extend([50, 60, 70])

# Remove the last element from numbers_list
numbers_list.pop()

# Sort numbers_list in ascending order
numbers_list.sort()

# Find and print the index of the value 30 in numbers_list
index_of_30 = numbers_list.index(30)

# Print the results
print("Final list:", numbers_list)
print("Index of 30:", index_of_30)
