import sqlite3


##connect to seqlite

connection = sqlite3.connect("student.db")

## create cursor object to insert
cursor = connection.cursor()

##create table

table_info = """
create table STUDENT (NAME VARCHAR(25), CLASS VARCHAR(25),
SECTION VARCHAR(25), MARKS INT)
"""

cursor.execute(table_info)

#insert more records
cursor.execute('''Insert Into STUDENT values('Priya','Psychology','A',95)''')
cursor.execute('''Insert Into STUDENT values('Poojith','Gen AI','A',97)''')
cursor.execute('''Insert Into STUDENT values('Jason','Data Science','B',80)''')
cursor.execute('''Insert Into STUDENT values('Prerana','Civil','C',74)''')
cursor.execute('''Insert Into STUDENT values('Devjith','Big Data','B',79)''')
cursor.execute('''Insert Into STUDENT values('Bujji','Data Science','C',66)''')

#display records

print("The inserted recoreds")
data = cursor.execute('''select * from STUDENT''')
for row in data:
    print(row)

##commit the changes

connection.commit()
connection.close()