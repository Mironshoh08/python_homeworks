# 1. Sort a Dictionary by Value
# Write a Python script to sort (ascending and descending) a dictionary by value.

# dict_1 = {"a": 3, "b": 1, "c": 5, "d": 2, "e": 4}
# print(sorted(key for key in dict_1.values()))  # asc
# print(sorted((key for key in dict_1.values()), reverse=True))  # desc

# 2. Add a Key to a Dictionary
# Write a Python script to add a key to a dictionary.
# Sample:
# {0: 10, 1: 20} 

# Expected Result:
# {0: 10, 1: 20, 2: 30}

# dict_1 = {0: 10, 1: 20}
# dict_1.update({2: 30})
# print(dict_1)

# 3. Concatenate Multiple Dictionaries
# Write a Python script to concatenate the following dictionaries to create a new one.
#
# Sample Dictionaries:
#
# dic1 = {1: 10, 2: 20}
# dic2 = {3: 30, 4: 40}
# dic3 = {5: 50, 6: 60}
# Expected Result:
#
# {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

# dic1 = {1: 10, 2: 20}
# dic2 = {3: 30, 4: 40}
# dic3 = {5: 50, 6: 60}
# dict_1 = {}
# for item in (dic1, dic2, dic3):
#     dict_1.update(item)
# print(dict_1)

# 4. Generate a Dictionary with Squares
# Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x).
#
# Sample Dictionary (n = 5):
#
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# n = 5
#
# dict_1 = {i: i ** 2 for i in range(1, n + 1)}
# print(dict_1)

# 5. Dictionary of Squares (1 to 15)
# Write a Python script to print a dictionary where the keys are numbers between 1 and 15 (both included) and the values are the square of the keys.
#
# Expected Output:
#
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225}

# dict_1 = {i: i ** 2 for i in range(1, 15 + 1)}
# print(dict_1)


# 1. Create a Set
# Write a Python program to create a set.

# set_1 = {1, 2, 3, 4, 5, 6}


# 2. Iterate Over a Set
# Write a Python program to iterate over sets.

# set_1 = {1, 2, 3, 4, 5, 6}
#
# for i in set_1:
#     print(i)


# 3. Add Member(s) to a Set
# Write a Python program to add member(s) to a set.

# set_1 = {1, 2, 3, 4, 5, 6}
#
# set_1 = list(set_1)
# set_1.append(7)
# print(set_1)

# 4. Remove Item(s) from a Set
# Write a Python program to remove item(s) from a given set.

# set_1 = {1, 2, 3, 4, 5, 6}
# set_1 = list(set_1)
# set_1.remove(6)
# print(set_1)

# 5. Remove an Item if Present in the Set
# Write a Python program to remove an item from a set if it is present in the set.

# set_1 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
# item_to_remove = 5
#
# if item_to_remove in set_1:
#     set_1.remove(item_to_remove)
#
# print(set_1)
