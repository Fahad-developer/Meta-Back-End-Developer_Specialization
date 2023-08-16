# Create a variable and use open function to open file.
# mode='r' represent what operation is going to be performed on a file.
file = open('text.txt', mode='r')

# Creating a variable and using readline() function to read and save data.
data = file.readline()

# Output data.
print(data)

# Closing the file.
file.close()

# Works same as above but have better exception handling.
# as file will create a variable called file.
with open('text.txt', mode='r') as file:
    data = file.readline()
    print(data)
