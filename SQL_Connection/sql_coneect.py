import mysql.connector
import difflib

con = mysql.connector.connect(
    user="ardit700_student",
    password="ardit700_student",
    host="108.167.140.122",
    database="ardit700_pm1database"
)

cursor = con.cursor()
word = ""
while (True):
    word = input("Enter a word: ")
    word = word.lower()
    query = cursor.execute("SELECT * FROM Dictionary WHERE Expression = '%s'" % word)
    results = cursor.fetchall()
    if results:
        for p in results:
            print(p)
    elif word == "ex-1":
        break
    else:
        print("The word don't exist, please write other one")
