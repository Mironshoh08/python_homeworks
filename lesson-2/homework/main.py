# 1. Age Calculator
# Write a Python program to ask for a user's name and year of birth, then calculate and display their age.

# name = input('Ismingizni kiriting: ')
# year = int(input('tug\'ilgan yilingizni kiriting: '))

# print(f'{name} siz {2025 - year} yoshadasiz')

# 2. Extract Car Names
# Extract car names from the following text:

# txt = 'LMaasleitbtui'

# car_name = txt[1::2]
# print(car_name)
# car_name = txt[::2]
# print(car_name)

# 3. Extract Car Names
# Extract car names from the following text:

# txt = 'MsaatmiazD'

# car_name = txt[::2]
# print(car_name)
# car_name = txt[-1::-2]
# print(car_name)

# 4. Extract Residence Area
# Extract the residence area from the following text:

# txt = "I'am John. I am from London"

# txt = txt.split()
# print(txt[5])

# 5. Reverse String
# Write a Python program that takes a user input string and prints it in reverse order.

# txt = input('Write Something: ')
# print(txt[::-1])

# 6. Count Vowels
# Write a Python program that counts the number of vowels in a given string.

# name = 'salimov'
# count = 0
# for i in name:
#     if i in 'aouie':
#         count += 1
#     else:
#         pass
#
# print(count)


# 7. Find Maximum Value
# Write a Python program that takes a list of numbers as input and prints the maximum value.

# lst = []
# while True:
#     numbers = input('Son Kiriting (exit): ')
#     if numbers.lower() == 'exit':
#         break
#     else:
#         lst.append(int(numbers))
# print(max(lst))

# 8. Check Palindrome
# Write a Python program that checks if a given word is a palindrome (reads the same forward and backward).

# def palindrome(text: str = 'bob'):
#     if text == text[::-1]:
#         return 'this text is palindrome'
#     return 'This text isn\'t palindrome'
#
#
# print(palindrome('kiyik'))


# 9. Extract Email Domain
# Write a Python program that extracts and prints the domain from an email address provided by the user.

# def extract_domain(email):
#     return email.split('@')[-1]
#
#
# # Example usage
# email = "salimov@gmail.com"
# print(extract_domain(email))


# 10. Generate Random Password
# Write a Python program to generate a random password containing letters, digits, and special characters.

# import random
# import string


# def generate_password(length=12):
#     characters = string.ascii_letters + string.digits + string.punctuation
#     password = ''.join(random.sample(characters, length))
#     return password


# print(generate_password())
