# Creating a Tuple.
my_tuple = (1, 'Strings', True, 4.2)

# Accessing Tuple values by their index.
print(my_tuple[1])

# Getting the Type of a Tuple.
print(type(my_tuple))

# .count method count the number of occurence of a value in the tuple.
print(my_tuple.count('Strings'))

# .index method return the index of an element in the tuple.
print(my_tuple.index(4.2))

# Iterating over a tuple.
for x in my_tuple:
    print("Value: ",x)


# We can also declare Tuples without parenthesis.

my_tuple_2 = 1, 'strings', True, 4.2
print(my_tuple_2)
