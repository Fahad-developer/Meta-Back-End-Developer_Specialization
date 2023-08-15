# Dictionary Dosn't allow duplicate values.

my_dic = {1: 'Test', 'Name': 'Jim'}

print(type(my_dic))

print(my_dic[1])

my_dic[2] = 'Test 2'

my_dic[1] = 'Not a test'

print(my_dic[1])

print(my_dic)

for key, value in my_dic.items():
    print(str(key) + " : " + value)
