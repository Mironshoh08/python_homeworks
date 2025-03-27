# 1. Modify String with Underscores
# Given a string txt, insert an underscore (_) after every third character. If a character is a vowel or already has an underscore after it, shift the underscore placement to the next character. No underscore should be added at the end.
#
# Examples
# Input: hello Output: hel_lo
#
# Input: assalom Output: ass_alom
#
# Input: abcabcabcdeabcdefabcdefg Output: abc_abc_abcd_abcd_abcdef

# ---

# chars = 'abcabcdabcdeabcdefabcdefg'
#
# vowel_chars = 'auieo'
#
# cnt = 2
# while cnt < len(chars):
#     if chars[cnt].lower() not in vowel_chars:
#         chars = chars[:cnt + 1] + '_' + chars[cnt:]
#         vowel_chars += chars[cnt]
#         cnt += 4
#         continue
#     cnt += 1
#
# print(chars)

# ---

# 2. Integer Squares Exercise
# Task
# The provided code stub reads an integer, n, from STDIN. For all non-negative integers i where 0 <= i < n, print i^2.
#
# Example Input
# 5
# Example Output
# 0
# 1
# 4
# 9
# 16
# Input Format
# The first and only line contains the integer, n.
#
# Constraints
# 1 <= n <= 20
# Output Format
# Print n lines, one corresponding to each i^2 where 0 <= i < n.

# def func_1(num: int):
#     for i in range(0, num):
#         print(i ** 2)
#
#
# func_1(5)

# ---

# 3. Loop-Based Exercises
# Exercise 1: Print first 10 natural numbers using a while loop

# cnt = 1
#
# while cnt != 10 + 1:
#     print(cnt)
#     cnt += 1

# ---

# Exercise 2: Print the following pattern
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

# n = int(input('Enter a number: '))
#
# lst = []
#
# for s in range(1, n + 1):
#     lst.append(s)
#     str_1 = ' '.join([str(s) for s in lst])
#     print(str_1)

# ---

# Exercise 3: Calculate sum of all numbers from 1 to a given number
# Example:
#
# Enter number 10
# Sum is: 55

# res = 0
# for i in range(1, (int(input('Enter a num: ')) + 1)):
#     res += i
# print(res)

# ---

# Exercise 4: Print multiplication table of a given number
# Example:

# 2
# 4
# 6
# 8
# 10
# 12
# 14
# 16
# 18
# 20

# for i in range(1, (int(input('Enter a num: ')) + 1)):
#     print(i * 2)

# ---

# numbers = [12, 75, 150, 180, 145, 525, 50]
#
# for i in numbers:
#     print(i)

# ---

# Exercise 6: Count the total number of digits in a number
# Example:
#
# 75869
# Output: 5

# print(len(str(input('Enter a number: '))))

# ---

# Exercise 7: Print reverse number pattern
# 5 4 3 2 1
# 4 3 2 1
# 3 2 1
# 2 1
# 1

# n = int(input('Enter a number: '))
#
# lst = []
#
# for s in range(5, 0, -1):
#     print(s, end=' ')
#     for i in range(s - 1, 0, -1):
#         print(i, end=' ')
#     print()

# ---

# Exercise 8: Print list in reverse order using a loop
# Given:
#
# list1 = [10, 20, 30, 40, 50]
# Expected Output:
#
# 50
# 40
# 30
# 20
# 10

# lst1 = [10, 20, 30, 40, 50]
#
# for i in reversed(lst1):
#     print(i)

# ---

# Exercise 9: Display numbers from -10 to -1 using a for loop
# -10
# -9
# -8
# -7
# -6
# -5
# -4
# -3
# -2
# -1

# for i in range(-10,0,1):
#     print(i)

# ---

# Exercise 10: Display message “Done” after successful loop execution
# Example:
#
# 0
# 1
# 2
# 3
# 4
# Done!

# for i in range(1, 10):
#     print(i)
# else:
#     print('Done')

# ---

# def is_prime(n):
#     if n <= 1:
#         return False
#     for i in range(2, int(n ** 0.5) + 1):
#         if n % i == 0:
#             return False
#     return True
#
#
# def generate_primes(start, end):
#     primes = []
#     for i in range(start, end + 1):
#         if is_prime(i):
#             primes.append(i)
#     return primes
#
#
# start = int(input("Enter the starting number: "))
# end = int(input("Enter the ending number: "))
#
# primes = generate_primes(start, end)
# for s in primes:
#     print(s)

# ---

# Exercise 12: Display Fibonacci series up to 10 terms
# Example:
#
# Fibonacci sequence:
# 0  1  1  2  3  5  8  13  21  34

# def fibonacci_series(num):
#     fibo = [0, 1]
#     for s in range(num - 2):
#         fibo.append(fibo[-1] + fibo[-2])
#     for a in fibo:
#         print(a,end=' ')
#
#
# fibonacci_series(10)

# ---

# Exercise 13: Find the factorial of a given number
# Example:
#
# 5! = 120

# def func_2(num):
#     if num in (0, 1):
#         return 1
#     else:
#         res = num * func_2(num - 1)
#         return res
#
#
# print(func_2(5))

# ---

# 4. Return Uncommon Elements of Lists
# Task
# Return the elements that are not common between two lists. The order of elements does not matter.
#
# Examples
# Input: list1 = [1, 1, 2], list2 = [2, 3, 4]
# Output: [1, 1, 3, 4]
#
# Input: list1 = [1, 2, 3], list2 = [4, 5, 6]
# Output: [1, 2, 3, 4, 5, 6]
#
# Input: list1 = [1, 1, 2, 3, 4, 2], list2 = [1, 3, 4, 5]
# Output: [2, 2, 5]

# def uncommon_elements(list1, list2):
#     result = []
#     for x in list1:
#         if x not in list2:
#             result.append(x)
#     for y in list2:
#         if y not in list1:
#             result.append(y)
#     return result
#
#
# print(uncommon_elements([1, 1, 2], [2, 3, 4]))
