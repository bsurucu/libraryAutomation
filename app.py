from os import system
import sqlite3
import time
db = sqlite3.connect("books.sqlite")
imlec = db.cursor()
imlec.execute("CREATE TABLE IF NOT EXISTS library (author, name)")
imlec.execute("CREATE TABLE IF NOT EXISTS users (id, password, isWorker)")


class Book():
    def __init__(self, name, author):
        self.name = author
        self.name = author

def addBook(name, author):
    add = "INSERT INTO library VALUES ('{}', '{}')".format(author, name)
    imlec.execute(add)
    db.commit()
    print("Book is added to the library!")

def removeBook(name, author):
    query = "SELECT * FROM library WHERE name = '{}' and author = '{}'".format(name, author)
    list = query
    if query:
        remove = "DELETE FROM library WHERE name = '{}' AND author = '{}'".format(name, author)
        imlec.execute(remove)
        db.commit()
        print("Book has been removed!")
    else:
        print("The book you want to remove is not found!")

def workerUI():
    while True:
        system("cls")
        print("""
        [1] Add Book
        [2] Remove Book
        """)
        workerOption = input("Your option: ")
        if workerOption == "1":
            name = input("Enter book name: ")
            author = input("Enter author name: ")
            addBook(name, author)
            input("Click 'enter' key to return to main menu!")

        elif workerOption == "2":
            name = input("Enter book name: ")
            author = input("Enter author name: ")
            removeBook(name, author)
            input("Click 'enter' key to return to main menu")

        else:
            print("Wrong input")
            input("Click 'enter' key to return main menu")




def customerUI():
    while True:
        print("""
        [1] Get Book
        [2] Redeem Book
        """)

        customerOption = input("Your option: ")

        if customerOption == "1":
            pass  # getBook()

        elif customerOption == "2":
            pass  # redeemBook()

        else:
            print("Wrong input")
            input("Press 'enter' key to leave")

while True:
    system("cls")
    print("""
    ==============================
    Welcome To Library!
    ==============================
    [1] Customer login
    [2] Worker login
    """)
    option = input("Your option: ")
    if option == "1":
        pass  # customer UI

    elif option == "2":
        ID = input("Enter your ID: ")
        PASSWORD = input("Enter your password: ")
        if ID == "2222" and PASSWORD == "1234":
            print("Succesfully logged in!")
            time.sleep(1)
            workerUI()
        else:
            print("Wrong input")
            input("Click 'enter' to return to main menu")

    else:
        print("Wrong input")
        print("Click 'enter' to return main menu")
        input()






db.close()
