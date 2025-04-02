import pandas as pd 
import datetime as dt

if os.path.exists('task\\stackoverflow_qa.csv'):
    print("stackoverflow_qa.csv fayli mavjud")
else:
    print("stackoverflow_qa.csv fayli mavjud emas")

if os.path.exists('task\\titanic.csv'):
    print("titanic.csv fayli mavjud")
else:
    print("titanic.csv fayli mavjud emas")

# filt = pd.to_datetime(df['creationdate']).dt.year < 2014

# print(df[filt])

# ---

# filt = pd.to_numeric(df['score']) > 50

# print(df[filt])

# ---

# filt = pd.to_numeric(df['score']).between(50,100)

# print(df[filt])

# ---
# filt = df['ans_name'] == 'Scott Boston'
# print(df[filt])

# ---

# users = ['User1', 'User2', 'User3', 'User4', 'User5']
# filtered_df = df[df['ans_name'].isin(users)]
# print(filtered_df)

# ---

# filt = (pd.to_datetime(df['creationdate']).between('2014-05-01','2014-10-01')) & (df['ans_name'] == 'Unutbu') & (pd.to_numeric(df['score']) < 5)

# print(df[filt])

# ---

# filt = pd.to_numeric(df['score'].between(5,10)) & (pd.to_numeric(df['viewcount'] > 10000))
# print(df[filt])

# ---

# filt = df['ans_name'] == 'Scott Boston'

# print(df[~filt])

# ---  #2

# new_df = df_1[(df_1['Sex'] == 'female') & (df_1['Pclass'] == 1) & (df_1['Age'].between(20,30))]
# print(new_df)

# ---

# new_df = df_1[df_1['Fare'] > 100]

# print(new_df)

# ---

# filt = (df_1['Survived'] == 1) & (df_1['SibSp'] == 0) & (df_1['Parch'] == 0)

# print(df_1[filt])

# ---

# new_df = df_1[(df_1['Embarked'] == 'C') & (df_1['Fare'] > 50)] 

# print(new_df)

# ---

# filt = (df_1['SibSp'] >= 1) & (df_1['Parch'] >= 1)

# print(df_1[filt])

# ---

# filt = (df_1['Age'] <= 15) & (df_1['Survived'] == 0)

# print(df_1[filt])

# ---

# filt = (df_1['Cabin'].notna()) & (df_1['Fare'] > 200)
# print(df_1[filt])

# ---

# new_df = df_1[df_1['PassengerId'] % 2 == 1]

# print(new_df) 

# --- 

# unique_tickets = df_1['Ticket'].value_counts()  
# unique_ticket_passengers = df_1[df_1['Ticket'].isin(unique_tickets[unique_tickets == 1].index)]

# print(unique_ticket_passengers)  

# ---

# filt = df_1[(df_1['Name'].str.contains('Miss')) & (df_1['Pclass'] == 1)]

# print(filt)

# ---

