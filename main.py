import mainMenu
import mainMenuNavigation
import db_table_creation

db_table_creation.createDatabase()

print("---------------------------------------------------------------------")
print()
print("                 WELCOME TO VG AIRLINE BOOKING !!                     ")
print()
print('''ALERT! DUE TO COVID TRAVEL RESTRICTIONS , We are currently operating 
flights to and from the following destinations:
    1. Dubai
    2. Delhi
    3. Singapore''')

mainMenuChoice = mainMenu.mainMenuDisplay()
mainMenuNavigation.mainMenuNavigation(mainMenuChoice)