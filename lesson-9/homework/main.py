# 1. Circle Class
# Write a Python program to create a class representing a Circle. Include methods to calculate its area and perimeter.

# import math
#
#
# class Circle:
#     def __init__(self, radius):
#         self.radius = radius
#
#     def area(self):
#         return math.pi * self.radius ** 2
#
#     def perimeter(self):
#         return 2 * math.pi * self.radius
#
#
# circle = Circle(5)
# print(circle.area())
# print(circle.perimeter())

# ---
# 2. Person Class
# Write a Python program to create a Person class. Include attributes like name, country, and date of birth. Implement a method to determine the person's age.

# from datetime import date
#
#
# class Person:
#     def __init__(self, name, country, birth_year):
#         self.name = name
#         self.country = country
#         self.birth_year = birth_year
#
#     def age(self):
#         current_year = date.today().year
#         return current_year - self.birth_year
#
#
# person = Person("Salimov", "Uzbekistan", 2008)
# print(person.age())

# ---

# 3. Calculator Class
# Write a Python program to create a Calculator class. Include methods for basic arithmetic operations.

# class Calculator:
#     @staticmethod
#     def add(self, a, b):
#         return a + b
#
#     @staticmethod
#     def subtract(self, a, b):
#         return a - b
#
#     @staticmethod
#     def multiply(self, a, b):
#         return a * b
#
#     @staticmethod
#     def divide(self, a, b):
#         if b == 0:
#             return "Cannot divide by zero"
#         return a / b
#
#
# calc = Calculator()
# print(calc.subtract(calc, 5, 3))
# print(calc.multiply(calc, 10, 2))

# ---
# 4. Shape and Subclasses
# Write a Python program to create a class that represents a shape. Include methods to calculate its area and perimeter. Implement subclasses for different shapes like Circle, Triangle, and Square.

# import math

# class Shape:
#     def area(self):
#         pass
#
#     def perimeter(self):
#         pass
#
#
# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius
#
#     def area(self):
#         return math.pi * self.radius ** 2
#
#     def perimeter(self):
#         return 2 * math.pi * self.radius
#
#
# class Square(Shape):
#     def __init__(self, side):
#         self.side = side
#
#     def area(self):
#         return self.side ** 2
#
#     def perimeter(self):
#         return 4 * self.side
#
#
# circle = Circle(4)
# square = Square(5)
# print(circle.perimeter())
# print(square.area())

# ---
# 5. Binary Search Tree Class
# Write a Python program to create a class representing a binary search tree. Include methods for inserting and searching for elements in the binary tree.

# class Node:
#     def __init__(self, key):
#         self.left = None
#         self.right = None
#         self.val = key
#
#
# class BST:
#     def __init__(self):
#         self.root = None
#
#     def insert(self, root, key):
#         if root is None:
#             return Node(key)
#         if key < root.val:
#             root.left = self.insert(root.left, key)
#         else:
#             root.right = self.insert(root.right, key)
#         return root
#
#     def search(self, root, key):
#         if root is None or root.val == key:
#             return root
#         if key < root.val:
#             return self.search(root.left, key)
#         return self.search(root.right, key)
#
#
# tree = BST()
# root = None
# root = tree.insert(root, 50)
# tree.insert(root, 30)
# tree.insert(root, 70)
# print(tree.search(root, 30) is not None)

# ---

# 6. Stack Data Structure
# Write a Python program to create a class representing a stack data structure. Include methods for pushing and popping elements.

# class Stack:
#     def __init__(self):
#         self.stack = []
#
#     def push(self, item):
#         self.stack.append(item)
#
#     def pop(self):
#         if not self.is_empty():
#             return self.stack.pop()
#         return "Stack is empty"
#
#     def is_empty(self):
#         return len(self.stack) == 0
#
#
# s = Stack()
# s.push(5)
# s.push(10)
# print(s.pop())

# ---

# 7. Linked List Data Structure
# Write a Python program to create a class representing a linked list data structure. Include methods for displaying linked list data, inserting, and deleting nodes.

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
#
#
# class LinkedList:
#     def __init__(self):
#         self.head = None
#
#     def insert(self, data):
#         new_node = Node(data)
#         new_node.next = self.head
#         self.head = new_node
#
#     def display(self):
#         current = self.head
#         while current:
#             print(current.data, end=" -> ")
#             current = current.next
#         print("None")
#
#
# ll = LinkedList()
# ll.insert(3)
# ll.insert(5)
# ll.display()

# ---

# 8. Shopping Cart Class
# Write a Python program to create a class representing a shopping cart. Include methods for adding and removing items, and calculating the total price.

# class ShoppingCart:
#     def __init__(self):
#         self.items = {}
#
#     def add_item(self, item, price):
#         self.items[item] = price
#
#     def remove_item(self, item):
#         if item in self.items:
#             del self.items[item]
#
#     def total_price(self):
#         return sum(self.items.values())
#
# cart = ShoppingCart()
# cart.add_item("Apple", 2)
# cart.add_item("Banana", 1)
# print(cart.total_price())


# ---

# 9. Stack with Display
# Write a Python program to create a class representing a stack data structure. Include methods for pushing, popping, and displaying elements.

# class Stack:
#     def __init__(self):
#         self.stack = []
#
#     def push(self, item):
#         self.stack.append(item)
#
#     def pop(self):
#         if self.stack:
#             return self.stack.pop()
#         return "Stack is empty"
#
#     def display(self):
#         print(self.stack)
#
#
# s = Stack()
# s.push(1)
# s.push(2)
# s.display()

# ---

# 10. Queue Data Structure
# Write a Python program to create a class representing a queue data structure. Include methods for enqueueing and dequeueing elements.

# class Queue:
#     def __init__(self):
#         self.queue = []
#
#     def enqueue(self, item):
#         self.queue.append(item)
#
#     def dequeue(self):
#         if self.queue:
#             return self.queue.pop(0)
#         return "Queue is empty"
#
# q = Queue()
# q.enqueue(10)
# q.enqueue(20)
# print(q.dequeue())

# ---

# 11. Bank Class
# Write a Python program to create a class representing a bank. Include methods for managing customer accounts and transactions.

# class Bank:
#     def __init__(self):
#         self.accounts = {}
#
#     def create_account(self, name, balance):
#         self.accounts[name] = balance
#
#     def deposit(self, name, amount):
#         if name in self.accounts:
#             self.accounts[name] += amount
#
#     def withdraw(self, name, amount):
#         if name in self.accounts and self.accounts[name] >= amount:
#             self.accounts[name] -= amount
#             return amount
#         return "Insufficient funds"
#
#
# bank = Bank()
# bank.create_account("Salimov", 102)
# bank.deposit("Mironshoh", 102)
# print(bank.withdraw("Salimov_1", 102))
