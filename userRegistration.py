import db_table_queries

def userRegistrationMenu():
    print("---------------------------------------------------------------------")
    print()
    print("WELCOME TO NEW USER REGISTERATION PORTAL")
    print()
    print("Select user type:")
    print(" a) Customer")
    print(" b) Staff")
    print(" c) Back to Main Menu")
    print()
    print("---------------------------------------------------------------------")
    print()
    userRegChoice = input("Enter your choice: ")

    return userRegChoice
    
def newCustomerRegisteration():
    print()
    print("Enter the following details -")
    email = input(" Email ID                  : ")
    password = input(" Password                  : ")
    passportNo = input(" Passport No.              : ")
    firstName = input(" First Name                : ")
    lastName = input(" Last Name                 : ")
    dob = input(" Date of Birth (YYYY-MM-DD): ")
    gender = input(" Gender                    : ")
    phoneNo = input(" Phone No.                 : ")
    address = input(" Address                   : ")
    city = input(" City                      : ")
    country = input(" Country                   : ")
    print()
    db_table_queries.addNewCustomer(email, password, passportNo, firstName, lastName, dob, gender, phoneNo, address, city, country)
    print()


def newStaffRegisteration():
    print()
    print("Enter the following details -")
    email = input(" Email ID                  : ")
    password = input(" Password                  : ")
    firstName = input(" First Name                : ")
    lastName = input(" Last Name                 : ")
    dob = input(" Date of Birth (YYYY-MM-DD): ")
    gender = input(" Gender                    : ")
    phoneNo = input(" Phone No.                 : ")
    print()
    db_table_queries.addNewStaff(email, password, firstName, lastName, dob, gender, phoneNo)
    print()

