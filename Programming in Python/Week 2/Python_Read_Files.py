with open('text.txt', 'r') as file:
    print(file.read(44))

    print(file.readline())

    print(file.readlines())
    data = file.read()

    for x in data:
        print(x)
