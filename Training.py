# # import sqlite3
# import sqlite3 
# connection = sqlite3.connect("Training.db") 
# cursor = connection.cursor() 
# cursor.execute("CREATE TABLE IF NOT EXISTS students (id INTEGER, name TEXT,grade REAL)")  
# # Add a student 
# # cursor.execute("INSERT INTO students (id, name, grade) VALUES (1, 'Alice', 85.5)") 
# # cursor.execute("INSERT INTO  students (id,name,grade) VALUES (2, 'Marvelous', 90.0)")
# # cursor.execute("UPDATE students SET grade = 95.0 WHERE name = 'Alice'")
# cursor.execute("SELECT * FROM  student WHERE name = 'Alice'")
# # cursor.execute("UPDATE students SET grade = 95.0 WHERE name = 'Bob'") 
# # connection.commit()
# # Save the changes 
# connection.commit() 
# # connection.close()

# import sqlite3
# connection= sqlite3.connect("food.db")
# cursor=connection.cursor()
# cursor.execute("CREATE TABLE IF NOT EXISTS Items (name TEXT, price  INTEGER )")
# # cursor.execute("INSERT INTO Items (name,price) VALUES ('beans' , 2222) ")
# # cursor.execute("SELECT price FROM Items WHERE name = 'beans'")
# # cursor.execute("UPDATE Items SET price= 2000 WHERE name = 'beans'")
# # cursor.execute("DELETE FROM Items WHERE name = 'beans'")
# # name = cursor.fetchone() 
# # print(name[0])
# connection.commit()
# connection.close()

# def hello (name):
#      return f"hello, {"akinwunmi"}!"

# def goodbye ("akinwunmi"):
#      return f"Goodbye,{"akinwunmi"}"#


import random

# Computer picks a random number
secret_number = random.randint(1, 50)

guess_count = 0
guess = None

print("Guess a number between 1 and 50")

while guess != secret_number:
    guess = int(input("Enter your guess: "))
    guess_count += 1

    if guess < secret_number:
        print("Too low!")
    elif guess > secret_number:
        print("Too high!")
    else:
        print("Correct! You guessed it!")
        print("You guessed the number in", guess_count, "tries!")