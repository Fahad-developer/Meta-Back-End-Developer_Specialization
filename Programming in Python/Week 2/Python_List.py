# List can have Alphabets.
list2 = ['A', 'B', 'C']

# List can have All type of values at once.
list3 = ['Hello', 1, True, 1.2]


# Within a list Index always starts from zero.
list1 = [1, 2, 3, 4, 5]
#        0  1  2  3  4


# Accessing value at index 2 
print(list1[2])

print(list1, sep = " ")

#Using * Symbol to Output the list. 
print(*list1)

#Another method to output the list.
print(list1)

# Inserting a value in the list1.
list1.insert(len(list1), 6)

print(list1, sep = " ")

# Insert a value at the end of a list.
list1.append(7)

print(list1, sep = " ")

# Extend the list and add 8, 9, 10 elements at the end of an list.
list1.extend([8, 9, 10])

print(list1, sep = " ")

# Removing a element using pop method.
list1.pop(9)

print(list1, sep = " ")


del list1[8]

print(list1, sep = " ")

# Iterating threw a list Uisng for loop.

for x in list1:
    print("Value: ",x)
