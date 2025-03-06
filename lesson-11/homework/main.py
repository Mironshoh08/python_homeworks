from custom_modules import math_operations as mt
from custom_modules import string_utils as st
from geometry.circle import calculate_area, calculate_circumference
from file_operations.file_writer import write_file
from file_operations.file_reader import read_file

# --- Math
print(mt.add(10, 5))
print(mt.subtract(10, 5))
# --- String
print(st.reverse_string("Python"))
print(st.count_vowels("hello world"))
# --- Geometry
print(calculate_area(7))
print(calculate_circumference(7))
# --- File
write_file("demo.txt", "Hello World!")
print(read_file("demo.txt"))
