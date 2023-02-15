import db_table_queries
from prettytable import PrettyTable

def searchFlightsMenu():
    print("---------------------------------------------------------------------")
    print()
    print("Search upcoming flights by city, airport, or date!")
    print()
    print(" a) Search by Departure and Arrival Destination")
    print(" b) Search by Date")
    print(" c) Back to Main Menu")
    print()
    print("---------------------------------------------------------------------")
    print()
    searchChoice = input("Enter your choice: ")

    return searchChoice
    
def searchByDepartureArrivalDestination():
    print()
    depCity = input("Enter Departure City : ")
    arrCity = input("Enter Arrival City   : ")
    result = db_table_queries.searchFlightsBasedOnCities(depCity,arrCity)
    if len(result)==0:
        print("No Flights between the selected cities!")
        print()
        print('''ALERT! DUE TO COVID TRAVEL RESTRICTIONS , We are currently operating 
                flights to and from the following destinations:
                1. Dubai
                2. Delhi
                3. Singapore''')

    else:
        x = PrettyTable()
        x.field_names = ["Flight Number","DepartureDate","DepartureTime","ArrivalDate","ArrivalTime","Price_Adult_Economy","Price_Adult_Business"]
            
        for value in result:
            x.add_row([value[0],value[2],value[3],value[5],value[6],value[9],value[10]])

        print(x)
    print()

def searchByDate():
    print()
    startDate = input("Enter Start Date : ")
    endDate = input("Enter End Date   : ")
    result = db_table_queries.searchFlightsBetween2Dates(startDate, endDate)
    if len(result)==0:
        print("No Flights between the selected dates!")
        
    else:
        x = PrettyTable()
        x.field_names = ["Flight Number","DepartureAirport","DepartureDate","DepartureTime","ArrivalAirport","ArrivalDate","ArrivalTime","Price_Adult_Economy","Price_Adult_Business"]
            
        for value in result:
            x.add_row([value[0],value[1],value[2],value[3],value[4],value[5],value[6],value[9],value[10]])

        print(x)
    print()