reserved_words = ["True", "False", "None", "is", "in", "and"]

my_string = "Hello, World!"

print(type(my_string), "Type ob")
print(id(my_string), "Id ob")

my_int = 77

print(type(my_int), "Type ob")
print(id(my_int))

# result_addition = my_string + str(my_int)
# my_str_to_int = int(my_string)
# result_subtraction = my_str_to_int - my_int

# num_1 = 36
# num_2 = 168
# num_3 = 25.65

# str_1 = str(num_1)
# str_2 = str(num_2)
# str_3 = str(num_3)

# num_from_str_1 = int(str_1)
# num_from_str_2 = int(str_2)
# num_from_str_3 = float(str_3)

name = "artem"
last_name = "anistratenko"
year = "16"
country = "ukraine"
pet = "slime"
book = "the lord of the rings"
play = "chess"
hobby = "video editing"
eat = "dumplings"

print(
    f"""My name is {name.capitalize()} and my last name {last_name.capitalize()}\n. About me:\t\nAge: {year}
      I live in {country.capitalize()}
      My favorite series books is {book.title()}
      My favorite game is {play.capitalize()}
      My hobby is {hobby.capitalize()}
      And my favorite food is {eat.capitalize()}"""
)

alphabet = "abcdefghijklmnopqrstuvwxyz"

word = (
    alphabet[5].upper()
    + alphabet[-9]
    + alphabet[4]
    + alphabet[4]
    + alphabet[3]
    + alphabet[-12]
    + alphabet[-14]
)
print(word)
original_text = "I hope you agree with me that the solution used above to deliver HTML to the browser is not good."
new_sentence = f"I hope that you {original_text[43:47]} {original_text[65:69]}."
print(original_text.find("HTML"))
print(new_sentence)
