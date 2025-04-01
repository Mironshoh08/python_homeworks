# import sqlite3

# conn = sqlite3.Connection('homework.sqlite')

# cursor = conn.cursor()

# create_database = ''' create table Roster (
#     Name int,
#     Species varchar(30),
#     Age varchar(30)
# ) '''
# cursor.execute(create_database)

# insert_query = ''' insert into Roster values ('Benjamin Sisko','Human',40),('Jadzia Dax','Trill',300),('Kira Nerys','Bajoran',29) '''
# cursor.execute(insert_query)

# update_query = ''' update Roster set name = 'Ezri Dax' where name = 'Jadzia Dax' '''
# cursor.execute(update_query)

# select_query = ''' select name,age from roster where Species = 'Bajoran' '''
# a = cursor.execute(select_query)
# print(a.fetchall())

# conn.commit()
# cursor.close()
# conn.close()
