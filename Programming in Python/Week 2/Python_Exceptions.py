# Create a Function to divide.
def divide_by(a, b):
    return a / b

# Try
try:
    print(divide_by(40, 0))

# Expect ZeroDivision error.
except ZeroDivisionError as e:
    print(e, "We cannot divide by zero.")
    print(e.__class__)


