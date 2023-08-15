# Sets do not allowed duplicate values and we can not print the values using index
#because set is unordered.

# Creating a set.
set_a = {1, 2, 3, 4, 5, 5}


# Adding a element in the set using .add method.
set_a.add(6)

# Remove an element from the set using .remove method.
set_a.remove(2)

# Remove an element from the set using .discard method.
set_a.discard(3)

print(set_a)

# Creating another set called set_b.
set_b = {4, 5, 6, 7, 8}


# Finding union using .union method.
print(set_a.union(set_b))
# OR
print(set_a | set_b)


# Finding intersection using .intersection method.
print(set_a.intersection(set_b))
# OR
print(set_a & set_b)

# Finding difference using .difference method.
print(set_a.difference(set_b))
# OR
print(set_a - set_b)

# Finding symmetric_difference using .symmetric_difference method.
print(set_a.symmetric_difference(set_b))
print(set_a ^ set_b)

# Iterating using for loop on/in a set.
for x in set_a:
    print("Values: ",x)
