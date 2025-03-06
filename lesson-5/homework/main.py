# 1. def is_leap(year): """ Determines whether a given year is a leap year.
#
# A year is a leap year if:
# - It is divisible by 4, and
# - It is NOT divisible by 100, unless it is also divisible by 400.
#
# Parameters:
# year (int): The year to be checked.
#
# Returns:
# bool: True if the year is a leap year, False otherwise.
# """
# if not isinstance(year, int):
#     raise ValueError("Year must be an integer.")
#
# return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

# def leap_year(year):
#     if not isinstance(year, int):
#         raise ValueError("Year must be an integer.")
#
#     return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
#
#
# print(leap_year(2000))


# 2. Conditional Statements Exercise
# Given an integer, n, perform the following conditional actions:
#
# If n is odd, print Weird
# If n is even and in the inclusive range of 2 to 5, print Not Weird
# If n is even and in the inclusive range of 6 to 20, print Weird
# If n is even and greater than 20, print Not Weird
# Input Format
# A single line containing a positive integer, n.
#
# Constraints
# 1 <= n <= 100
# Output Format
# Print Weird if the number is weird. Otherwise, print Not Weird.
#
# Sample Input 0
# 3
# Sample Output 0
# Weird

# def weird(n):
#     if n % 2 == 1:
#         print("Weird")
#     elif 2 <= n <= 5:
#         print("Not Weird")
#     elif 6 <= n <= 20:
#         print("Weird")
#     else:
#         print("Not Weird")
#
#
# weird(3)


# 3. Given two integer numbers a and b. Find even numbers between this numbers. a and b are inclusive. Don't use loop.
# Give two solutions.
#
# Solution 1 with if-else statement.
# Solution 2 without if-else statement.

# --- 1

# def with_if_else(a, b):
#     if a % 2 != 0:
#         a += 1
#
#     if b % 2 != 0:
#         b -= 1
#
#     return list(range(a, b + 1, 2))


# print(with_if_else(3, 10))


# --- 2

# def without_if_else(a, b):
#     return list(range(a + (a % 2), b + 1 - (b % 2), 2))


# print(without_if_else(3, 10))
