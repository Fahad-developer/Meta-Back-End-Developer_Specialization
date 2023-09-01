# Creating a Class
class DemoClass:
    # Making a variable in class.
    a = 10
    # Creating a Function inside a Class.
    def sumvalue(self):
        print(20 + 30)


# Creating a Object.
demoobject = DemoClass()
demoobject1 = DemoClass()
# Calling Object and variable.
print(demoobject.a)
print(demoobject1.a)
# Calling Function using Object.
demoobject.sumvalue()