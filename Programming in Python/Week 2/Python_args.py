# Instead of passing in just two arguments, 
# args will allow n arguments to come through any number of arguments.

def sum_of(*args):
    sum = 0
    for x in args:
        sum += x
    return sum

print(sum_of(4, 5, 6, 7, 5, 2, 1))
