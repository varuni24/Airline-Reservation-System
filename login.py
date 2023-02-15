import db_table_queries
from prettytable import PrettyTable

def loginDetails():
    print("---------------------------------------------------------------------")

    print()
    print("WELCOME TO EXISTING USER LOGIN PORTAL")
    print()

    username = input("Username/Email: ")
    password = input("Password: ")
    
    print()
    print("Choose Login Mode:")
    print(" a) Customer")
    print(" b) Staff")
    print(" c) Back to Main Menu")
    print()

    loginMode = input("Enter your login mode: ")
    
    print()
    print("---------------------------------------------------------------------")
    
    return [username,password,loginMode]



########## CUSTOMER ##########

def customerLoginWelcome(customerDetails):
    print()
    print("Welcome", customerDetails[3].upper(),customerDetails[4].upper(),"!")
    print()

def customerLoginMenu():
    print("---------------------------------------------------------------------")
    print()
    print("CUSTOMER MENU")
    print()
    print("Choose from the following:")
    print(" a) Make New Booking")
    print(" b) Cancel Booking")
    print(" c) Update Personal Details")
    print(" d) View My Bookings")
    print(" e) View Personal Details")
    print(" f) Logout")
    print()
    customerMenuChoice = input("Enter your choice: ")
   
    return customerMenuChoice


def customerMakeBooking(customerDetails):

    deptCity=input("Enter deprature city : ")
    arrCity=input("Enter arrival city   : ")
    print()
    result = db_table_queries.searchDuringBooking(deptCity,arrCity)

    if len(result)!=0:
        x = PrettyTable()
        x.field_names = ["Flight Number","Departure Date","Departure Time","Arrival Date", "Arrival Time","Price_Adult_Economy", "Price_Adult_Business"]
        for value in result:
            x.add_row(list(value))
        print("FLIGHT DETAILS")
        print()
        print(x)

        print()
        flightNo = input("Enter Flight No. : ")

        if(db_table_queries.checkIfFlightExists(flightNo)):
            noOfPassengers = int(input("Enter no of passengers you want to book for: "))
            print()
            
            passengerDetails = []
            
            print("Details of the Passengers:-")
            print()

            for i in range(noOfPassengers):

                print("---- DETAILS OF PASSENGER", i+1,"----")
                passengerFirstName = input("Enter first name              : ")
                passengerLastName = input("Enter last name               : ")
                passengerPassport = input("Enter passport no             : ")
                passengerDOB = input("Enter DOB                     : ")
                passengerAge = input("Enter age                     : ")
                passengerClass = input("Enter class (business/economy): ")
                print()

                passengerDetails.append((passengerFirstName, passengerLastName, passengerPassport, passengerDOB, passengerAge, passengerClass))

            totalPrice = calculatePrice(passengerDetails, flightNo)
            print("The total price is", totalPrice)
            confirm = input("Do you wish to continue ? Enter y/n : ")
            if(confirm.lower() == "y"):
                db_table_queries.bookTicket(customerDetails[0], passengerDetails, flightNo)
            else:
                print("You have declined your payment.")
        
        else:
            print("Flight does not exist")
    
    print()


def calculatePrice(passengerDetails, flightNo):
    
    flightDetails = db_table_queries.getFlightDetails(flightNo)
    totalPrice = 0

    for passenger in passengerDetails:
        
        if int(passenger[4]) <= 12:
            if passenger[5].lower() == "economy":
                totalPrice = totalPrice + float(flightDetails[9])
            else:
                totalPrice = totalPrice + float(flightDetails[10])
        
        elif int(passenger[4]) >= 60:
            if passenger[5].lower() == "economy":
                totalPrice = totalPrice + float(flightDetails[13])
            else:
                totalPrice = totalPrice + float(flightDetails[14])

        else:
            if passenger[5].lower() == "economy":
                totalPrice = totalPrice + float(flightDetails[11])
            else:
                totalPrice = totalPrice + float(flightDetails[12])

    return totalPrice


def customerCancelBooking(customerDetails):
    print()
    ticketId = input("Enter the ticket id: ")
    customerEmail = customerDetails[0] 
    db_table_queries.cancelBooking(ticketId, customerEmail)
    print()


def updateCustomerDetails(customerDetails):
    print()
    print("Select the detail that you would like to update -")
    print(" a) Password")
    print(" b) Passport No.")
    print(" c) First Name")
    print(" d) Last Name")
    print(" e) Date of Birth")
    print(" f) Gender")
    print(" g) Phone Number")
    print(" h) Address")
    print(" i) City")
    print(" j) Country")
    print(" k) Go back to Main Menu")
    print()
    updateCustomerChoice = input("Enter your choice: ")
    if updateCustomerChoice.lower() !=  "k":
        db_table_queries.updateSpecificCustomerDetail(customerDetails[0],updateCustomerChoice)
    else:
        print("Wrong option entered!")
    print()



def viewCustomerBookings(customerDetails):
    print()

    bookings = db_table_queries.viewBookings(customerDetails[0])
    
    if(len(bookings)!=0):
        x = PrettyTable()
        x.field_names = ["Ticket ID","Flight Number","Airline Name","First Name", "Last Name", "Passport Number"," Class","Departure Date","Arrival Date","Departure Time","Arrival Time"]
        for booking in bookings:
            x.add_row(list(booking))
        print("Your upcoming bookings -")
        print()
        print(x)
    
    else:
         print("You do not have any bookings.")

    print()

def viewCustomerDetails(customerDetails):
    print()
    result = db_table_queries.viewCustomerDetails(customerDetails[0])
    if(len(result) != 0):
        x = PrettyTable()
        x.field_names = ["Email ID","Password","Passport Number","First Name", "Last Name"," Date of Birth","Gender","Phone No","Address","City","Country"]
        for value in result:
            x.add_row(list(value))
        print("Your details are as follows:-")
        print()
        print(x)
    print()


########## STAFF ##########

def staffLoginWelcome(staffDetails):
    print() 
    print("Welcome", staffDetails[2].upper(),staffDetails[3].upper(),"!")
    print()


def staffLoginMenu():
    print("---------------------------------------------------------------------")
    print()
    print("STAFF MENU")
    print()
    print("Choose from the following:")
    print(" a) View flights")
    print(" b) Add Flight")
    print(" c) Change Flight Status")
    print(" d) Update Personal Details")
    print(" e) View Personal Details")
    print(" f) Back to Main Menu")
    print()
    staffMenuChoice = input("Enter your choice: ")
   
    return staffMenuChoice


def staffViewFlights():
    print()
    print("Search upcoming flights by arrival city, departure city, or date!")
    print()
    print(" a) Search by Departure Destination")
    print(" b) Search by Arrival Destination")
    print(" c) Search by Departure Date")
    print(" d) Search by Arrival Date")
    print(" e) Back to Main Menu")
    print()
    staffViewChoice = input("Enter your choice: ")

    if staffViewChoice.lower() == "a":
        depCity = input("Enter departure destination : ")
        result = db_table_queries.searchFlightBasedonDepCity(depCity)
        if len(result) == 0:
            print("No flights for this departure city!")
            print('''ALERT! DUE TO COVID TRAVEL RESTRICTIONS , We are currently operating flights to and from the following destinations:
                1. Dubai
                2. Delhi
                3. Singapore''')
        else:
            x = PrettyTable()
            x.field_names = ["Flight Number","DepartureDate","DepartureTime","ArrivalAirport","ArrivalDate","ArrivalTime","Price_Adult_Economy","Price_Adult_Business"]
            
            for value in result:
                x.add_row([value[0],value[2],value[3],value[4],value[5],value[6],value[9],value[10]])

            print(x)
    
    elif staffViewChoice.lower() == "b":
        arrCity = input("Enter arrival destination : ")
        result  = db_table_queries.searchFlightBasedonArrCity(arrCity)
        if len(result) == 0:
            print("No flights for this arrival city!")
            print('''ALERT! DUE TO COVID TRAVEL RESTRICTIONS , We are currently operating flights to and from the following destinations:
                1. Dubai
                2. Delhi
                3. Singapore''')
        else:
            x = PrettyTable()
            x.field_names = ["Flight Number","DepartureAirport","DepartureDate","DepartureTime","ArrivalDate","ArrivalTime","Price_Adult_Economy","Price_Adult_Business"]
            
            for value in result:
                x.add_row([value[0],value[1],value[2],value[3],value[4],value[6],value[9],value[10]])

            print(x)
   
    elif staffViewChoice.lower() == "c":
        depDate = input("Enter departure date : ")
        result  = db_table_queries.searchFlightBasedonDepDate(depDate)
        if len(result) == 0:
            print("No flights for this departure date!")
        else:
            x = PrettyTable()
            x.field_names = ["Flight Number","DepartureAirport","DepartureTime","Arrival Airport","ArrivalDate","ArrivalTime","Price_Adult_Economy","Price_Adult_Business"]
            
            for value in result:
                x.add_row([value[0],value[1],value[3],value[4],value[5],value[6],value[9],value[10]])

            print(x)

    elif staffViewChoice.lower() == "d":
        arrDate = input("Enter arrival date : ")
        result  = db_table_queries.searchFlightBasedonArrDate(arrDate)
        if len(result) == 0:
            print("No flights for this arrival date!")
        else:
            x = PrettyTable()
            x.field_names = ["Flight Number","DepartureAirport","DepartureDate","DepartureTime","Arrival Airport","ArrivalTime","Price_Adult_Economy","Price_Adult_Business"]
            
            for value in result:
                x.add_row([value[0],value[1],value[2],value[3],value[4],value[6],value[9],value[10]])

            print(x)
    
    elif staffViewChoice.lower() == "e":
        print("")

    else:
        print("Wrong option entered!")

    print()


def staffAddFlights():
    print()
    airline = input("Enter airline: ")
    flightNo = input("Enter flight no: ")
    depAirport = input("Enter departure airport: ")
    arrAirport = input("Enter arrival airport: ")
    depDate = input("Enter departure date: ")
    arrDate = input("Enter arrival date: ")
    depTime = input("Enter departure time: ")
    arrTime = input("Enter arrival time: ")

    print()
    print("ECONOMY CLASS PRICE: ")
    priceChildEconomy = input("Child: ")
    priceAdultEconomy = input("Adult: ")
    priceSeniorEconomy = input("Senior: ")
    print()
    print("BUSINESS CLASS PRICE: ")
    priceChildBusiness = input("Child: ")
    priceAdultBusiness = input("Adult: ")
    priceSeniorBusiness = input("Senior: ")
    print()
    db_table_queries.addNewFlight(airline,flightNo,depAirport,arrAirport,depDate,arrDate,depTime,arrTime,priceChildEconomy,priceAdultEconomy,priceSeniorEconomy,priceChildBusiness,priceAdultBusiness,priceSeniorBusiness)
    print()


def staffChangeFlightStatus():
    print()
    airlineName = input("Enter Airline Name   : ")
    flightNo = input("Enter Flight No      : ")
    status = input("Enter Updated Status : ")

    db_table_queries.changeFlightStatus(status, flightNo, airlineName)

    print()


def updateStaffDetails(staffDetails):
    print()
    print("Select the detail that you would like to update -")
    print(" a) Password")
    print(" b) First Name")
    print(" c) Last Name")
    print(" d) Date of Birth")
    print(" e) Gender")
    print(" f) Phone Number")
    print(" g) Go back to Main Menu")

    print()
    updateStaffChoice = input("Enter your choice: ")

    if updateStaffChoice.lower() !=  "g":
        db_table_queries.updateSpecificStaffDetail(staffDetails[0],updateStaffChoice)
    else:
        print("Wrong option entered!")

    print()



def viewStaffDetails(staffDetails):
    print()
    result = db_table_queries.viewStaffDetails(staffDetails[0])
    if(len(result) != 0):
        x = PrettyTable()
        x.field_names = ["Email ID","Password","First Name", "Last Name"," Date of Birth","Gender","Phone No"]
        for value in result:
            x.add_row(list(value))
        print("Your details are as follows:-")
        print()
        print(x)

    print()
