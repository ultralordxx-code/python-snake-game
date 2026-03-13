# # def hello (name):
# #     return f"hello, {name}!"

# # def goodbye (name):
# #     return f"Goodbye,{name} !"


# # import sqlite3

# # # connect to the database
# # conn = sqlite3.connect("school.db")
# # cursor 

# import sqlite3
  
#  # Connect to database
# connection = sqlite3.connect("class.db")
# cursor = connection.cursor()

# cursor.execute("CREATE  TABLE IF NOT EXISTS food(id INTEGER, food TEXT, price INTEGER)")

# cursor.execute("INSERT INTO food (id, food, price) VALUES (1, )") 
# cursor.execute
# cursor.execute("select * FROM  students")
# all_students=cursor.fetchall()
# print(all_students)
# cursor.execute("UPDATE students SET grade = 5.0 WHERE name ='Bob'")
# cursor.execute("SELECT  food list FROM  WHERE price = 1500")
# name = cursor.fetchone()
# print(name[0])
#  #add a student
# cursor.execute("INSERT INTO students (id,name,grade) VALUES(1, 'Alice', 85.5)")
# cursor.execute ("INSERT INTO students (id,name, grade) VALUES ( 1, 'Alice', 85.5)")
# # # # cursor.executemany('INSERT INTO Students (id,name,grade )VALUES(?,?,?)', Student_list)
# # cursor.execute ("SELECT * FROM Shoppin")
# # all_shoppin=cursor.fetchone()
# # print(all_shoppin)
# connection.commit()
# connection.close




import sqlite3
# # try:
# # Connect to database
connection = sqlite3.connect("Shoppin_list.db")
cursor = connection.cursor()
cursor.execute("CREATE  TABLE IF NOT EXISTS Students(id INTEGER,name TEXT,grade REAL)")
cursor.execute("INSERT INTO students (id,name,grade) VALUES(4, 'Dana',88.0")

connection.commit()
connection.close