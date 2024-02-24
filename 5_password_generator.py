import random
uppercase_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
lowercase_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
count_uppercase_letters = int(input("How many uppercase letters would you like in your password?\n"))
count_lowercase_letters = int(input("How many lowercase letters would you like?\n"))
count_symbols = int(input("How many symbols would you like?\n"))
count_numbers = int(input("How many numbers would you like?\n"))

password = ""
for letter in range(0, count_uppercase_letters + 1):
    password += random.choice(uppercase_letters)
for letter in range(0, count_lowercase_letters + 1):
    password += random.choice(lowercase_letters)
for symbol in range(0, count_symbols + 1):
    password += random.choice(symbols)
for number in range(0, count_numbers + 1):
    password += random.choice(numbers)

password_list = list(password)
random.shuffle(password_list)
password = ''.join(password_list)

print(f"Here is your password: {password}")
input()
