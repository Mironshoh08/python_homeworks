# Homework 1. ToDo List Application
#
# Define Task Class:
# Create a Task class with attributes such as task title, description, due date, and status.
# Define ToDoList Class:
# Create a ToDoList class that manages a list of tasks.
# Include methods to add a task, mark a task as complete, list all tasks, and display incomplete tasks.
# Create Main Program:
# Develop a simple CLI to interact with the ToDoList.
# Include options to add tasks, mark tasks as complete, list all tasks, and display only incomplete tasks.
# Test the Application:
# Create instances of tasks and test the functionality of your ToDoList.

# class Task:
#     def __init__(self, task_title, task_description, task_due_date):
#         self.title = task_title
#         self.description = task_description
#         self.due_date = task_due_date
#         self.completed = False

#     def mark_complete(self):
#         self.completed = True

#     def __str__(self):
#         status = "Completed" if self.completed else "Incomplete"
#         return f"{self.title} - {self.description} (Due: {self.due_date}) [{status}]"


# class TodoList:
#     def __init__(self):
#         self.tasks = []

#     def add_task(self, task_title, task_description, task_due_date):
#         task = Task(task_title, task_description, task_due_date)
#         self.tasks.append(task)
#         return "Task added successfully!"

#     def mark_task_complete(self, task_title):
#         for task in self.tasks:
#             if task.title == task_title:
#                 task.mark_complete()
#                 return f"Task '{task_title}' marked as complete."
#         return "Task not found."

#     def list_tasks(self):
#         return "\n".join(str(task) for task in self.tasks) if self.tasks else "No tasks available."

#     def list_incomplete_tasks(self):
#         incomplete_tasks = [str(task) for task in self.tasks if not task.completed]
#         return "\n".join(incomplete_tasks) if incomplete_tasks else "No incomplete tasks."


# todo_list = TodoList()

# while True:
#     print("\nTo-Do List Application")
#     print("1. Add Task")
#     print("2. Mark Task as Complete")
#     print("3. List All Tasks")
#     print("4. List Incomplete Tasks")
#     print("5. Exit")
#     command = input("Choose an option: ")

#     if command == "1":
#         title = input("Task Title: ")
#         description = input("Task Description: ")
#         due_date = input("Due Date: ")
#         print(todo_list.add_task(task_title=title, task_description=description, task_due_date=due_date))
#     elif command == "2":
#         title = input("Enter task title to mark as complete: ")
#         print(todo_list.mark_task_complete(task_title=title))
#     elif command == "3":
#         print("\nAll Tasks:")
#         print(todo_list.list_tasks())
#     elif command == "4":
#         print("\nIncomplete Tasks:")
#         print(todo_list.list_incomplete_tasks())
#     elif command == "5":
#         print("Exiting To-Do List Application...")
#         break
#     else:
#         print("Invalid option, please try again.")


# ---

# Homework 2. Simple Blog System
#
# Define Post Class:
# Create a Post class with attributes like title, content, and author.
# Define Blog Class:
# Create a Blog class that manages a list of posts.
# Include methods to add a post, list all posts, and display posts by a specific author.
# Create Main Program:
# Develop a CLI to interact with the Blog system.
# Include options to add posts, list all posts, and display posts by a specific author.
# Enhance Blog System:
# Add functionality to delete a post, edit a post, and display the latest posts.
# Test the Application:
# Create instances of posts and test the functionality of your Blog system.


# class Post:
#     def __init__(self, post_title, post_content, post_author):
#         self.title = post_title
#         self.content = post_content
#         self.author = post_author

#     def __str__(self):
#         return f"Title: {self.title}\nAuthor: {self.author}\nContent: {self.content}\n"


# class Blog:
#     def __init__(self):
#         self.posts = []

#     def add_post(self, blog_title, blog_content, blog_author):
#         post = Post(blog_title, blog_content, blog_author)
#         self.posts.append(post)

#     def list_posts(self):
#         return "\n".join(str(post) for post in self.posts) if self.posts else "No posts available."

#     def list_posts_by_author(self, blog_author):
#         filtered_posts = [post for post in self.posts if post.author == blog_author]
#         return "\n".join(str(post) for post in filtered_posts) if filtered_posts else "No posts by this author."

#     def delete_post(self, blog_title):
#         for post in self.posts:
#             if post.title == blog_title:
#                 self.posts.remove(post)
#                 return f"Post '{blog_title}' deleted."
#         return "Post not found."

#     def edit_post(self, blog_title, blog_new_content):
#         for post in self.posts:
#             if post.title == blog_title:
#                 post.content = blog_new_content
#                 return f"Post '{blog_title}' updated."
#         return "Post not found."

#     def latest_posts(self, count=5):
#         latest = self.posts[-count:] if len(self.posts) >= count else self.posts
#         return "\n".join(str(post) for post in reversed(latest)) if latest else "No posts available."


# blog = Blog()

# while True:
#     print("\nBlog System")
#     print("1. Add Post")
#     print("2. List All Posts")
#     print("3. List Posts by Author")
#     print("4. Delete Post")
#     print("5. Edit Post")
#     print("6. Show Latest Posts")
#     print("7. Exit")
#     choice = input("Choose an option: ")

#     if choice == "1":
#         title = input("Post Title: ")
#         content = input("Post Content: ")
#         author = input("Author: ")
#         blog.add_post(title, content, author)
#         print("Post added successfully!")
#     elif choice == "2":
#         print("\nAll Posts:")
#         print(blog.list_posts())
#     elif choice == "3":
#         author = input("Enter author's name: ")
#         print(blog.list_posts_by_author(author))
#     elif choice == "4":
#         title = input("Enter post title to delete: ")
#         print(blog.delete_post(title))
#     elif choice == "5":
#         title = input("Enter post title to edit: ")
#         new_content = input("Enter new content: ")
#         print(blog.edit_post(title, new_content))
#     elif choice == "6":
#         print("\nLatest Posts:")
#         print(blog.latest_posts())
#     elif choice == "7":
#         print("Exiting...")
#         break
#     else:
#         print("Invalid option, please try again.")


# ---

# Homework 3. Simple Banking System
#
# Define Account Class:
# Create an Account class with attributes like account number, account holder name, and balance.
# Define Bank Class:
# Create a Bank class that manages a list of accounts.
# Include methods to add an account, check balance, deposit money, and withdraw money.
# Create Main Program:
# Develop a CLI to interact with the Banking system.
# Include options to add accounts, check balance, deposit money, and withdraw money.
# Enhance Banking System:
# Add functionality to transfer money between accounts, display account details, and handle account overdrafts.
# Test the Application:
# Create instances of accounts and test the functionality of your Banking system.

# class Account:
#     def __init__(self, account_number, holder_name, account_balance=0):
#         self.account_number = account_number
#         self.holder_name = holder_name
#         self.balance = account_balance

#     def deposit(self, account_amount):
#         self.balance += account_amount
#         return f"Deposited {account_amount}. New balance: {self.balance}"

#     def withdraw(self, account_amount):
#         if account_amount > self.balance:
#             return "Insufficient funds."
#         self.balance -= account_amount
#         return f"Withdrew {account_amount}. New balance: {self.balance}"

#     def __str__(self):
#         return f"Account: {self.account_number}, Holder: {self.holder_name}, Balance: {self.balance}"


# class Bank:
#     def __init__(self):
#         self.accounts = []

#     def add_account(self, account_number, holder_name, account_balance=0):
#         account = Account(account_number, holder_name, account_balance)
#         self.accounts.append(account)
#         return "Account created successfully."

#     def get_account(self, account_number):
#         for account in self.accounts:
#             if account.account_number == account_number:
#                 return account
#         return None

#     def check_balance(self, account_number):
#         account = self.get_account(account_number)
#         return f"Balance: {account.balance}" if account else "Account not found."

#     def deposit_money(self, account_number, deposit_amount):
#         account = self.get_account(account_number)
#         return account.deposit(deposit_amount) if account else "Account not found."

#     def withdraw_money(self, account_number, withdraw_amount):
#         account = self.get_account(account_number)
#         return account.withdraw(withdraw_amount) if account else "Account not found."

#     def transfer_money(self, from_account, to_account, amount_1):
#         sender = self.get_account(from_account)
#         receiver = self.get_account(to_account)

#         if not sender or not receiver:
#             return "One or both accounts not found."

#         if sender.balance < amount_1:
#             return "Insufficient funds."

#         sender.withdraw(amount_1)
#         receiver.deposit(amount_1)
#         return f"Transferred {amount_1} from {from_account} to {to_account}."


# bank = Bank()

# while True:
#     print("\nBanking System")
#     print("1. Create Account")
#     print("2. Check Balance")
#     print("3. Deposit Money")
#     print("4. Withdraw Money")
#     print("5. Transfer Money")
#     print("6. Exit")
#     choice = input("Choose an option: ")

#     if choice == "1":
#         acc_num = input("Account Number: ")
#         name = input("Account Holder Name: ")
#         balance = int(input("Initial Balance: "))
#         print(bank.add_account(acc_num, name, balance))
#     elif choice == "2":
#         acc_num = input("Enter Account Number: ")
#         print(bank.check_balance(acc_num))
#     elif choice == "3":
#         acc_num = input("Enter Account Number: ")
#         amount = float(input("Enter Deposit Amount: "))
#         print(bank.deposit_money(acc_num, amount))
#     elif choice == "4":
#         acc_num = input("Enter Account Number: ")
#         amount = float(input("Enter Withdrawal Amount: "))
#         print(bank.withdraw_money(acc_num, amount))
#     elif choice == "5":
#         from_acc = input("Enter Sender Account Number: ")
#         to_acc = input("Enter Receiver Account Number: ")
#         amount = float(input("Enter Transfer Amount: "))
#         print(bank.transfer_money(from_acc, to_acc, amount))
#     elif choice == "6":
#         print("Exiting...")
#         break
#     else:
#         print("Invalid option, please try again.")
