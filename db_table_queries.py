import mysql.connector
import random


mydb = mysql.connector.connect(host="localhost", user="root", password="root", database="Project_Varuni")
mycursor = mydb.cursor()

def generateNDigitRandom(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return random.randint(range_start, range_end)



#### ADD NEW USER ####

def addNewCustomer(email, password, passportNo, firstName, lastName, dob, gender, phoneNo, address, city, country):

    sqlQuery = "INSERT INTO CUSTOMER VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    sqlParams = (email, password, passportNo, firstName, lastName, dob, gender, phoneNo, address, city, country)
    try:
        mycursor.execute(sqlQuery, sqlParams)
        mydb.commit()
        print("Customer Added!")
    except:
        print("An error occured! Try again!")




def addNewStaff(email, password, firstName, lastName, dob, gender, phoneNo):

    sqlQuery = "INSERT INTO AIRLINESTAFF VALUES(%s, %s, %s, %s, %s, %s, %s)"
    sqlParams = (email, password, firstName, lastName, dob, gender, phoneNo)
    try:
        mycursor.execute(sqlQuery, sqlParams)
        mydb.commit()
        print("Staff Member Added!")
    except:
        print("An error occured! Try again!")



#### AUTHENTICATION ####

def authenticateCustomer(email,password):

    sqlQuery = "SELECT * FROM CUSTOMER WHERE CEmail = %s and CPassword = %s"
    sqlParams = (email,password)
    mycursor.execute(sqlQuery,sqlParams)
    result = mycursor.fetchall()
    return [len(result), result]




def authenticateStaff(email,password):

    sqlQuery = "SELECT * FROM AIRLINESTAFF WHERE SEmail = %s and SPassword = %s"
    sqlParams = (email,password)
    mycursor.execute(sqlQuery,sqlParams)
    result = mycursor.fetchall()
    return [len(result), result]



#### SEARCH FLIGHTS ####

def searchFlightsBetween2Dates(startDate, endDate):

    sqlQuery = "SELECT * FROM FLIGHT WHERE (DepartureDate BETWEEN %s AND %s) OR (ArrivalDate BETWEEN %s and %s)"
    sqlParams = (startDate, endDate, startDate, endDate)
    mycursor.execute(sqlQuery,sqlParams)
    result = mycursor.fetchall()
    return result


def searchDuringBooking(depCity,arrCity):
    mycursor.execute("SELECT AirportName FROM AIRPORT WHERE AirportCity=%s",(depCity,))
    depAirportResult = mycursor.fetchall()
        
    mycursor.execute("SELECT AirportName FROM AIRPORT WHERE AirportCity=%s",(arrCity,))
    arrAirportResult = mycursor.fetchall()

    if(len(depAirportResult) == 0 or len(arrAirportResult) == 0):

        print("No flights to and from these destinations are available")
        print('''ALERT! DUE TO COVID TRAVEL RESTRICTIONS , We are currently operating 
        flights to and from the following destinations:
        1. Dubai
        2. Delhi
        3. Singapore''')
        return[]

    else:
        sqlQuery = "SELECT FlightNo, DepartureDate, DepartureTime, ArrivalDate, ArrivalTime,Price_Adult_Economy, Price_Adult_Business FROM FLIGHT WHERE DepartureAirport = %s AND ArrivalAirport = %s"
        sqlParams = (depAirportResult[0][0], arrAirportResult[0][0])
        mycursor.execute(sqlQuery,sqlParams)
        result = mycursor.fetchall()
        return result

def searchFlightsBasedOnCities(depCity, arrCity):
    
    mycursor.execute("SELECT AirportName FROM AIRPORT WHERE AirportCity=%s",(depCity,))
    depAirportResult = mycursor.fetchall()
        
    mycursor.execute("SELECT AirportName FROM AIRPORT WHERE AirportCity=%s",(arrCity,))
    arrAirportResult = mycursor.fetchall()

    if(len(depAirportResult) == 0 or len(arrAirportResult) == 0):
        return []
    else:
        sqlQuery = "SELECT * FROM FLIGHT WHERE DepartureAirport = %s AND ArrivalAirport = %s"
        sqlParams = (depAirportResult[0][0], arrAirportResult[0][0])
        mycursor.execute(sqlQuery,sqlParams)
        result = mycursor.fetchall()
        return result




def searchFlightBasedonDepCity (depCity):

    mycursor.execute("SELECT AirportName FROM AIRPORT WHERE AirportCity=%s",(depCity,))
    depAirportResult = mycursor.fetchall()
    if len(depAirportResult) == 0:
        return []
    else:
        sqlQuery = "SELECT * FROM FLIGHT WHERE DepartureAirport = %s"
        sqlParams = (depAirportResult[0][0],)
        mycursor.execute(sqlQuery,sqlParams)
        result = mycursor.fetchall()
        return result




def searchFlightBasedonArrCity (arrCity):

    mycursor.execute("SELECT AirportName FROM AIRPORT WHERE AirportCity=%s",(arrCity,))
    arrAirportResult = mycursor.fetchall()
    if len(arrAirportResult) == 0:
        return []
    else:
        sqlQuery = "SELECT * FROM FLIGHT WHERE ArrivalAirport = %s"
        sqlParams = (arrAirportResult[0][0],)
        mycursor.execute(sqlQuery,sqlParams)
        result = mycursor.fetchall()
        return result




def searchFlightBasedonDepDate (depDate):

    sqlQuery = "SELECT * FROM FLIGHT WHERE DepartureDate = %s"
    sqlParams = (depDate,)
    mycursor.execute(sqlQuery,sqlParams)
    result = mycursor.fetchall()
    return result




def searchFlightBasedonArrDate (arrDate):

    sqlQuery = "SELECT * FROM FLIGHT WHERE ArrivalDate = %s"
    sqlParams = (arrDate,)
    mycursor.execute(sqlQuery,sqlParams)
    result = mycursor.fetchall()
    return result




#### UPDATE DETAILS ####

def updateSpecificCustomerDetail(customerEmail, choice):
    
    if choice.lower() == "a":
        newPassword = input("Enter new Password: ")
        mycursor.execute("UPDATE CUSTOMER SET CPassword = %s WHERE CEmail = %s",(newPassword,customerEmail))
    
    elif choice.lower() == "b":
        newPassportNo = input("Enter new Passport No : ")
        mycursor.execute("UPDATE CUSTOMER SET CPassportNo = %s WHERE CEmail = %s",(newPassportNo,customerEmail))
    
    elif choice.lower() == "c":
        newFirstName = input("Enter new First Name: ")
        mycursor.execute("UPDATE CUSTOMER SET CFirstName = %s WHERE CEmail = %s",(newFirstName,customerEmail))
    
    elif choice.lower() == "d":
        newLastName = input("Enter new Last Name: ")
        mycursor.execute("UPDATE CUSTOMER SET CLastName = %s WHERE CEmail = %s",(newLastName,customerEmail))
    
    elif choice.lower() == "e":
        newDOB = input("Enter new DOB: ")
        mycursor.execute("UPDATE CUSTOMER SET CDateOfBirth = %s WHERE CEmail = %s",(newDOB,customerEmail))
    
    elif choice.lower() == "f":
        newGender = input("Enter new Gender: ")
        mycursor.execute("UPDATE CUSTOMER SET CGender = %s WHERE CEmail = %s",(newPasnewGendersword,customerEmail))
    
    elif choice.lower() == "g":
        newPhoneNo = input("Enter new Phone No: ")
        mycursor.execute("UPDATE CUSTOMER SET CPhoneNo = %s WHERE CEmail = %s",(newPhoneNo,customerEmail))
    
    elif choice.lower() == "h":
        newAddress = input("Enter new Address: ")
        mycursor.execute("UPDATE CUSTOMER SET CAddress = %s WHERE CEmail = %s",(newAddress,customerEmail))
    
    elif choice.lower() == "i":
        newCity = input("Enter new City: ")
        mycursor.execute("UPDATE CUSTOMER SET CCity = %s WHERE CEmail = %s",(newCity,customerEmail))
    
    elif choice.lower() == "j":
        newCountry = input("Enter new Country: ")
        mycursor.execute("UPDATE CUSTOMER SET CCountry = %s WHERE CEmail = %s",(newCountry,customerEmail))
    
    else:
        print("Wrong option entered")
        
    if choice.lower() in ["a","b","c","d","e","f","g","h","i","j"]:
        mydb.commit()
        print("Field updated!")




def updateSpecificStaffDetail(staffEmail, choice):

    if choice.lower() == "a":
        newPassword = input("Enter new Password: ")
        mycursor.execute("UPDATE AIRLINESTAFF SET SPassword = %s WHERE SEmail = %s",(newPassword,staffEmail))
    
    elif choice.lower() == "b":
        newFirstName = input("Enter new First Name: ")
        mycursor.execute("UPDATE AIRLINESTAFF SET SFirstName = %s WHERE SEmail = %s",(newFirstName,staffEmail))
    
    elif choice.lower() == "c":
        newLastName = input("Enter new Last Name: ")
        mycursor.execute("UPDATE AIRLINESTAFF SET SCLastName = %s WHERE SEmail = %s",(newLastName,staffEmail))
    
    elif choice.lower() == "d":
        newDOB = input("Enter new DOB: ")
        mycursor.execute("UPDATE AIRLINESTAFF SET SDateOfBirth = %s WHERE SEmail = %s",(newDOB,staffEmail))
    
    elif choice.lower() == "e":
        newGender = input("Enter new Gender: ")
        mycursor.execute("UPDATE AIRLINESTAFF SET SGender = %s WHERE SEmail = %s",(newPasnewGendersword,staffEmail))
    
    elif choice.lower() == "f":
        newPhoneNo = input("Enter new Phone No: ")
        mycursor.execute("UPDATE AIRLINESTAFF SET SPhoneNo = %s WHERE SEmail = %s",(newPhoneNo,staffEmail))
    
    else:
        print("Wrong option entered")
        
    if choice.lower() in ["a","b","c","d","e","f"]:
        mydb.commit()
        print("Field updated!")
    



#### CHANGE FLIGHT STATUS ####

def changeFlightStatus(status, flightNo, airlineName):

    mycursor.execute("SELECT AirlineID FROM AIRLINE WHERE AirlineName = %s",(airlineName,))
    airlineIdResult = mycursor.fetchall()

    if(len(airlineIdResult) == 0):
        print("Invalid details entered!")
    else:
        airlineID = airlineIdResult[0][0]
        sqlQuery = "UPDATE flight SET FlightStatus = %s WHERE FlightNo = %s AND AirlineID = %s"
        sqlParams = (status, flightNo, airlineID)
        mycursor.execute(sqlQuery,sqlParams)
        mydb.commit()
        result = mycursor.fetchall()




#### CANCEL TICKET BOOKING ####

def cancelBooking(ticketId, customerEmail):

    mycursor.execute("SELECT * FROM TICKET WHERE TicketID = %s",(ticketId,))
    noOfRows = mycursor.fetchall()

    if(len(noOfRows) != 0):
        sqlQuery = "UPDATE TICKET SET TicketStatus = %s WHERE TicketID = %s AND CustomerEmail = %s" 
        sqlParams = ("CANCELLED", ticketId, customerEmail)
        try:
            mycursor.execute(sqlQuery,sqlParams)
            mydb.commit()
            print("Your ticket has been successfully cancelled!")
        except:
            print("An error occured! Please try again later!")

    else:
        print("No such booking found!")




#### ADD FLIGHT ####

def addNewFlight(airline,flightNo,depAirport,arrAirport,depDate,arrDate,depTime,arrTime,priceChildEconomy,priceAdultEconomy,priceSeniorEconomy,priceChildBusiness,priceAdultBusiness,priceSeniorBusiness):

    airlineId = checkIfAirlineExists(airline)

    sqlQuery = "INSERT INTO FLIGHT VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    sqlParams = (flightNo,depAirport ,depDate ,depTime,arrAirport,arrDate,arrTime,"None",airlineId,priceChildEconomy,priceChildBusiness,priceAdultEconomy,priceAdultBusiness,priceSeniorEconomy,priceSeniorBusiness)
    
    try:
        mycursor.execute(sqlQuery,sqlParams)
        mydb.commit()
        print("Flight Added!")
    except:
        print("An error occured! Try again!")




def checkIfAirlineExists(airlineName):
    mycursor.execute("SELECT AirlineID from AIRLINE WHERE AirlineName = %s",(airlineName,))
    result = mycursor.fetchall()
    
    if(len(result) == 0):

        mycursor.execute("SELECT DISTINCT AirlineId from AIRLINE ")
        result = mycursor.fetchall()

        if result == []:
            newId = generateNDigitRandom(5)
            mycursor.execute("INSERT INTO AIRLINE(AirlineId, AirlineName) VALUES (%s,%s)",(newId,airlineName))
            mydb.commit()
        
        else:
            flag = True
            while (flag):
                for tuple in result:
                    newId = generateNDigitRandom(5)
                    if newId not in tuple:
                        mycursor.execute("INSERT INTO AIRLINE(AirlineId, AirlineName) VALUES (%s,%s)",(newId,airlineName))
                        mydb.commit()
                        flag = False

        return newId

    else:
        mycursor.execute("SELECT AirlineId FROM AIRLINE WHERE AirlineName = %s",(airlineName,))
        IDResult = mycursor.fetchall
        return IDResult[0][0]
    



def getFlightDetails(flightNo):
    mycursor.execute("SELECT * from FLIGHT WHERE FlightNo = %s",(flightNo,))
    result = mycursor.fetchall()
    if len(result) == 0:
        return ()
    else:
        return result[0]




def bookTicket(customerEmail, passengerDetails, flightNo):
    
    mycursor.execute("SELECT AirlineName from AIRLINE, FLIGHT WHERE FLIGHT.FlightNo = %s AND FLIGHT.AirlineID = AIRLINE.AirlineID",(flightNo,))
    result = mycursor.fetchall()
    airlineName = result[0][0]

    for passenger in passengerDetails:
        
        mycursor.execute("SELECT DISTINCT TicketID FROM TICKET")
        tickets = mycursor.fetchall()

        if tickets == []:
            ticketId = generateNDigitRandom(6)
            passenger = list(passenger)
            passenger.append(str(ticketId))
            passenger = tuple(passenger)
            sqlQuery = "INSERT INTO TICKET(TicketID,AirlineName,FlightNo,TicketStatus,CustomerEmail) VALUES (%s,%s,%s,%s,%s)"
            sqlParams = (ticketId, airlineName, flightNo, "RESERVED", customerEmail)
            mycursor.execute(sqlQuery,sqlParams)
            mydb.commit()
        
        else:
            flag = True
            while (flag):
                for ticket in tickets:
                    ticketId = generateNDigitRandom(6)
                    if ticketId not in ticket:
                        passenger = list(passenger)
                        passenger.append(str(ticketId))
                        passenger = tuple(passenger)
                        mycursor.execute("INSERT INTO TICKET(TicketID,AirlineName,FlightNo,TicketStatus,CustomerEmail) VALUES (%s,%s,%s,%s,%s)",(ticketId, airlineName, flightNo, "RESERVED", customerEmail))
                        mydb.commit()
                        flag = False
                        break

        sqlQuery = "INSERT INTO PASSENGER_DETAILS(PassengerFirstName, PassengerLastName, PassengerPassport, PassengerDOB, PassengerAge, PassengerClass, TicketID) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        sqlParams = passenger
        mycursor.execute(sqlQuery, sqlParams)
        mydb.commit()

    print()
    print("Your  tickets have been booked :) ")




def checkIfFlightExists(flightNo):
    mycursor.execute("SELECT DISTINCT FlightNo FROM FLIGHT")
    flights = mycursor.fetchall()
    for flight in flights:
        if flightNo in flight:
            return True
    return False


def viewBookings(customerEmail):
    sqlQuery = '''SELECT TICKET.TicketID, FLIGHT.FlightNo,TICKET.AirlineName, PASSENGER_DETAILS.PassengerFirstName, PASSENGER_DETAILS.PassengerLastName, PASSENGER_DETAILS.PassengerPassport, PASSENGER_DETAILS.PassengerClass, FLIGHT.DepartureDate, FLIGHT.ArrivalDate, FLIGHT.DepartureTime, FLIGHT.ArrivalTime
                FROM TICKET
                JOIN PASSENGER_DETAILS ON TICKET.TicketID = PASSENGER_DETAILS.TicketID
                JOIN FLIGHT ON FLIGHT.FlightNo = TICKET.FlightNo            
                WHERE CustomerEmail = %s AND TicketStatus='RESERVED' '''

    mycursor.execute(sqlQuery,(customerEmail,))
    results=mycursor.fetchall()
    return results
    

def viewCustomerDetails(customerEmail):
    try:
        mycursor.execute("SELECT * FROM CUSTOMER WHERE CEmail = %s",(customerEmail,))
        results=mycursor.fetchall()
        return results
    except:
        print("Error fetching details! Try Again!")
        return []


def viewStaffDetails(staffEmail):
    try:
        mycursor.execute("SELECT * FROM AIRLINESTAFF WHERE SEmail = %s",(staffEmail,))
        results=mycursor.fetchall()
        return results
    except:
        print("Error fetching details! Try Again!")
        return []