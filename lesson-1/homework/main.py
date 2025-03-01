# Given a side of square. Find its perimeter and area.
# Given diameter of circle. Find its length.
# Given two numbers a and b. Find their mean.
# Given two numbers a and b. Find their sum, product and square of each number.

a = int(input('A Side: '))
print(f"""Perimetr : {a * 4}
Area : {a ** 2}
""")

diametr = int(input('Diametr: '))
print(3.14 * diametr)

num_1 = int(input('Num 1: '))
num_2 = int(input('Num 2: '))
print((num_1 + num_2) / 2)

num_1 = int(input('Num 1: '))
num_2 = int(input('Num 2: '))

print(f"""Sum: {num_1 + num_2}
Product: {num_1 * num_2}
Square Num_1: {num_1 ** 2}
Square Num_2: {num_2 ** 2}
""")
