# import greetings
# print(greetings.hello("alice"))

# import calculator
# print(calculator)
# file =open("example.txt", "a" )
# file.write("hello, world!\n")
# file.write(" you are one of the 1%.")
# file.close()

# file = open ("shopping_.txt", "a")

# content=file.write("what do u want to buy")

# file.close()

# import calculator
# print(calculator)


# import random

# generate a random number between 1 and 100
# number = random.randint(1, 100)

# print("Random number between 1 and 100:", number)


# rates = {
#     "EUR": 0.93,
#     "NGN": 1400,
#     "GBP": 0.78
# }

# def convert_usd(amount, currency):
#     return amount * rates[currency]

# print(convert_usd(10, "EUR"))
# # print(convert_usd(10, "NGN"))


# import csv 

# with open ("data.csv", "w", newline="") as file:
#     writer = csv.writer(file)
#     writer.writerow(["name", "age", "country"])
#     writer.writerow(["Alice","25","USA"])
#     writer.writerow(["Bob", "30", "canada"])



# with open ("data.csv",  "r") as file:
#     reader = csv.reader(file)
#     for row in reader:
#         print(row)

# import json

# Data ={"name": "alice","age": 25, "city": "new york"}

# with open ("Data.json", "w")as file:
#     json.dump(Data,file)

# with open ("data.json","r") as file:
#     loaded_data=json.load(file)
#     print(loaded_data)


# import os
# if os.path.exists("example.txt"):
#     os.remove("example.txt")
# else:
#     print("file does not exist")


# with open("shopping.txt", "a") as file:
#      item= input("what is your item?")
#      file.write(f"{item}\n")
     
import sqlite3
# food
