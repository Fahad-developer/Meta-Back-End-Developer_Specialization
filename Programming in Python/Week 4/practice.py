class person:
    def __init__(self, name, age, number):
        self.name = name
        self.age = age
        if age > 18:
            print("Valid age.")
        else:
            print("Invalid age.")

        self.number = number

    def __str__(self):
        return f"{self.name}({self.age})"

    def myfunc(self):
        print("Hello my name is " + self.name)


obj = person("Fahad", 23, 923101800)

print(obj.name)
print(obj.age)
obj.myfunc()

