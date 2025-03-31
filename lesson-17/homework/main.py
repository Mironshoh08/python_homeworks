# import numpy as np
# import pandas as pd

# data = {
#     'First Name': ['Alice', 'Bob', 'Charlie', 'David'], 
#     'Age': [25, 30, 35, 40], 
#     'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago']
#     }
# df = pd.DataFrame(data)
# df.set_index('First Name')
# ---
# 1. Rename column names using function. "First Name" --> "first_name", "Age" --> "age

# df = df.rename(columns={'First Name': 'first_name', 'Age': 'age'})

# ---
# 2. Print the first 3 rows of the DataFrame

# print(df[1:4])

# ---
# 3.Find the mean age of the individuals

# print(df['Age'].mean())

# ---
# 4. Select and print only the 'Name' and 'City' columns

# print(df[['First Name','City']])

# ---
# 5. Add a new column 'Salary' with random salary values

# df['Salary'] = np.random.randint(100,500,size=len(df))

# ---
# 6. Display summary statistics of the DataFrame

# print(df.describe())

# 2.1 Create a DataFrame named sales_and_expenses with columns 'Month', 'Sales', and 'Expenses', representing monthly sales and expenses data. Use below table.

# data = {
#     'Month': ['Jan', 'Feb', 'Mar', 'Apr'],
#     'Sales': [5000, 6000, 7500, 8000],
#     'Expenses': [3000, 3500, 4000, 4500]
# }

# sales_and_expenses = pd.DataFrame(data)

# 2.2 Calculate and display the maximum sales and expenses.

# sales_max = sales_and_expenses['Sales'].max()
# expenses_max = sales_and_expenses['Expenses'].max()

# print(f'Max sales: {sales_max},\nMax expenses: {expenses_max}')

# 2.3 Calculate and display the minimum sales and expenses.

# sales_min = sales_and_expenses['Sales'].min()
# expenses_min = sales_and_expenses['Expenses'].min()

# print(f'Min sales: {sales_min},\nMin expenses: {expenses_min}')

# 2.4 Calculate and display the average sales and expenses.

# avg_sales = sales_and_expenses['Sales'].mean()
# avg_expenses = sales_and_expenses['Expenses'].mean()

# print(f'AVG sales: {avg_sales},\nAVG expenses: {avg_expenses}')


# 3.1 Create a DataFrame named expenses with columns 'Category', 'January', 'February', 'March', and 'April', representing monthly expenses for different categories. Use below table.

# data = {
#     'Category': ['Rent', 'Utilities', 'Groceries', 'Entertainment'],
#     'January': [1200, 200, 300, 150],
#     'February': [1300, 220, 320, 160],
#     'March': [1400, 240, 330, 170],
#     'April': [1500, 250, 350, 180]
# }
 
# expenses = pd.DataFrame(data)
# expenses = expenses.set_index('Category')


# 3.2 Calculate and display the maximum expense for each category.

# max_expenses = expenses.max(axis=1)

# print(max_expenses)

# 3.3 Calculate and display the minimum expense for each category.

# min_expenses = expenses.min(axis=1)

# print(min_expenses)

# 3.4 Calculate and display the average expense for each category.

# avg_expenses = expenses.mean(axis=1)

# print(avg_expenses)

