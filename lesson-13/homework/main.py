# from datetime import date, time, datetime, timedelta
# import pytz
# import re

# 1. Age Calculator: Ask the user to enter their birthdate. Calculate and print their age in years, months, and days.

# user_birthdate = input('Enter your birth date (Format YYYY-mm-dd): ')
# user_birthdate = datetime.strptime(user_birthdate, '%Y-%m-%d').date()

# today = date.today()

# years = today.year - user_birthdate.year
# months = today.month - user_birthdate.month
# days = today.day - user_birthdate.day
 
# if days < 0:
#     months -= 1
#     days += (today.replace(month=today.month - 1 if today.month > 1 else 12, day=1) - user_birthdate.replace(month=user_birthdate.month - 1 if user_birthdate.month > 1 else 12, day=1)).days

# if months < 0:
#     years -= 1
#     months += 12

# print(f'Age: {years}, months: {months}, days:{days}')

# 2. Days Until Next Birthday: Similar to the first exercise, but this time, calculate and print the number of days remaining until the user's next birthday.
 

# birth_date = input("Enter your birthdate (YYYY-MM-DD): ")
# birth_date = datetime.strptime(birth_date, "%Y-%m-%d")
# today = datetime.today()

# next_birthday = birth_date.replace(year=today.year)
# if next_birthday < today:
#     next_birthday = next_birthday.replace(year=today.year + 1)

# days_until = (next_birthday - today).days
# print(f"Days until next birthday: {days_until}")


# 3. Meeting Scheduler: Ask the user to enter the current date and time, as well as the duration of a meeting in hours and minutes. Calculate and print the date and time when the meeting will end.
 

# current_date = input("Enter the current date and time (YYYY-MM-DD HH:MM): ")
# duration_hours = int(input("Enter meeting duration (hours): "))
# duration_minutes = int(input("Enter meeting duration (minutes): "))

# current_datetime = datetime.strptime(current_date, "%Y-%m-%d %H:%M")
# end_datetime = current_datetime + timedelta(hours=duration_hours, minutes=duration_minutes)

# print(f"Meeting will end at: {end_datetime.strftime('%Y-%m-%d %H:%M')}")


# 4. Timezone Converter: Create a program that allows the user to enter a date and time along with their current timezone, and then convert and print the date and time in another timezone of their choice.
 

# date_time = input("Enter date and time (YYYY-MM-DD HH:MM): ")
# current_timezone = input("Enter current timezone (e.g., UTC, US/Eastern): ")
# target_timezone = input("Enter target timezone (e.g., Europe/London): ")

# dt = datetime.strptime(date_time, "%Y-%m-%d %H:%M")
# current_tz = pytz.timezone(current_timezone)
# target_tz = pytz.timezone(target_timezone)

# dt = current_tz.localize(dt)
# converted_time = dt.astimezone(target_tz)

# print(f"Converted time: {converted_time.strftime('%Y-%m-%d %H:%M %Z')}")

# 5. Countdown Timer: Implement a countdown timer. Ask the user to input a future date and time, and then continuously print the time remaining until that point in regular intervals (e.g., every second).
 
# future_time = input("Enter a future date and time (YYYY-MM-DD HH:MM:SS): ")
# future_time = datetime.strptime(future_time, "%Y-%m-%d %H:%M:%S")

# while True:
#     now = datetime.now()
#     remaining_time = future_time - now
#     if remaining_time.total_seconds() <= 0:
#         print("Time's up!")
#         break
#     print(f"Time remaining: {remaining_time}")
#     time.sleep(1)

# 6. Email Validator: Write a program that validates email addresses. Ask the user to input an email address, and check if it follows a valid email format.
 
# email = input("Enter an email address: ")
# pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"

# if re.match(pattern, email):
#     print("Valid email address.")
# else:
#     print("Invalid email address.")

# 7. Phone Number Formatter: Create a program that takes a phone number as input and formats it according to a standard format. For example, convert "1234567890" to "(123) 456-7890".

# phone = input("Enter a 10-digit phone number: ")
# phone = re.sub(r"\D", "", phone)

# if len(phone) == 10:
#     formatted_phone = f"({phone[:3]}) {phone[3:6]}-{phone[6:]}"
#     print(f"Formatted Phone Number: {formatted_phone}")
# else:
#     print("Invalid phone number. Please enter a 10-digit number.")

# 8. Password Strength Checker: Implement a password strength checker. Ask the user to input a password and check if it meets certain criteria (e.g., minimum length, contains at least one uppercase letter, one lowercase letter, and one digit).
  
# password = input("Enter a password: ")

# length = len(password) >= 8
# uppercase = re.search(r"[A-Z]", password)
# lowercase = re.search(r"[a-z]", password)
# digit = re.search(r"\d", password)

# if length and uppercase and lowercase and digit:
#     print("Strong password.")
# else:
#     print("Weak password. Make sure it has at least 8 characters, one uppercase, one lowercase, and one digit.")

# 9. Word Finder: Develop a program that finds all occurrences of a specific word in a given text. Ask the user to input a word, and then search for and print all occurrences of that word in a sample text.

# text = input("Enter a text: ")
# word = input("Enter the word to find: ")

# words = text.lower().split()
# count = words.count(word.lower())

# print(f"The word '{word}' appears {count} times.")

# 10. Date Extractor: Write a program that extracts dates from a given text. Ask the user to input a text, and then identify and print all the dates present in the text.
  
# text = input("Enter a text: ")
# date_pattern = r"\b\d{4}-\d{2}-\d{2}\b|\b\d{2}/\d{2}/\d{4}\b|\b\d{2}-\d{2}-\d{4}\b"

# dates = re.findall(date_pattern, text)

# if dates:
#     print("Extracted dates:", ", ".join(dates))
# else:
#     print("No dates found.")
