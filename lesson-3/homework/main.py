# 1. Create and Access List Elements
# Create a list containing five different fruits and print the third fruit.

# lst_fruit = ['apple', 'orange', 'pineapple', 'banana', 'mango']
#
# print(lst_fruit[2])


# 2. Concatenate Two Lists
# Create two lists of numbers and concatenate them into a single list.

# lst_1 = [1, 2, 3, 4, 5, 6]
# lst_2 = [7, 8, 9, 10, 11]
#
# print(lst_1 + lst_2)

# 3. Extract Elements from a List
# Given a list of numbers, extract the first, middle, and last elements and store them in a new list.

# lst = [0, 1, 2, 3, 4, 5, 6, 7, 8]
# new_lst = lst[0], lst[4], lst[-1]
# print(new_lst)

# 4. Convert List to Tuple
# Create a list of your five favorite movies and convert it into a tuple.

# lst = ['The Social Network', 'In Time', 'Wonka', 'Home Alone 2', 'Hillbilly Elegy']  # for_example
#
# lst = tuple(lst)
#
# print(type(lst))


# 5. Check Element in a List
# Given a list of cities, check if "Paris" is in the list and print the result.

# lst_cities = ['New york', 'London', 'Tokyo', 'Los Angeles', 'Paris']
#
# for i in lst_cities:
#     if i.lower() == 'paris':
#         print(lst_cities)
#     else:
#         pass

# 6. Duplicate a List Without Using Loops
# Create a list of numbers and duplicate it without using loops.

# from copy import deepcopy
#
# lst = [1, 2, 3, 4, 5, 6]
#
# lst_1 = deepcopy(lst)
#
# print(lst_1)


# 7. Swap First and Last Elements of a List
# Given a list of numbers, swap the first and last elements.

# lst = [1, 2, 3, 4, 5, 6]
# lst[0], lst[-1] = 6, 1
#
# print(lst)


# 8. Slice a Tuple
# Create a tuple of numbers from 1 to 10 and print a slice from index 3 to 7.

# lst = [i for i in range(1, 10 + 1)]
#
# print(lst[3:7])

# 9. Count Occurrences in a List
# Create a list of colors and count how many times "blue" appears in the list.

# lst = ['green', 'blue', 'red', 'cyan', 'blue']
#
# count = 0
# for i in lst:
#     if i.lower() == 'blue':
#         count += 1
#     else:
#         pass
#
# print(count)

# 10. Find the Index of an Element in a Tuple
# Given a tuple of animals, find the index of "lion".

# lst = ['fox', 'tiger', 'lion', 'monkey']
# index = lst.index('lion')
#
# print(index)

# 11. Merge Two Tuples
# Create two tuples of numbers and merge them into a single tuple.

# tuple = (1, 2, 3, 4, 5, 6)
# tuple_1 = (3, 4, 5, 6, 7, 8)
#
# merged_tuple = tuple(set(tuple + tuple_1))
# print(merged_tuple)

# 12. Find the Length of a List and Tuple
# Given a list and a tuple, find and print their lengths.

# lst = ['salimov', 'Mironshoh', 16]
# tuple = ['salimov', 'Mironshoh', 16]
#
# print(len(lst))
# print(len(tuple))


# 13. Convert Tuple to List
# Create a tuple of five numbers and convert it into a list.

# tpl = (1, 2, 3, 4, 5, 6)
# tpl = list(tpl)
#
# print(type(tpl))


# 14. Find Maximum and Minimum in a Tuple
# Given a tuple of numbers, find and print the maximum and minimum values.

# tuple = (1, 2, 3, 4, 5, 6)
# print(max(tuple))


# 15. Reverse a Tuple
# Create a tuple of words and print it in reverse order.

# tuple = (1, 2, 3, 4, 5, 6, 7)
# tuple = list(tuple)
# print(tuple[::-1])
