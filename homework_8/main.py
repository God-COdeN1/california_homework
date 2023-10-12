reserved_words = ["True", "False", "None", "is", "in", "and"]

my_string = "Hello, World!"

print(type(my_string), "Type ob")
print(id(my_string), "Id ob")

my_int = 77

print(type(my_int), "Type ob")
print(id(my_int))

result_addition = my_string + str(my_int)
my_str_to_int = int(my_string)
result_subtraction = my_str_to_int - my_int

# Перетворення числового типу даних в строку і навпаки
num_1 = 36
num_2 = 168
num_3 = 25.65

str_1 = str(num_1)
str_2 = str(num_2)
str_3 = str(num_3)

num_from_str_1 = int(str_1)
num_from_str_2 = int(str_2)
num_from_str_3 = float(str_3)
