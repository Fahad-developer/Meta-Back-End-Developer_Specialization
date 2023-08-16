# We can also write:
# with open('newfile.txt'. 'w') as file:
try:
    with open('Newfile.txt', mode='w') as file:
        file.write("This is a new line.")
        file.writelines(["We are writting multiple lines", "\n We can write multi[le lines."])
except FileNotFoundError as e:
    print("ERROR", e)
