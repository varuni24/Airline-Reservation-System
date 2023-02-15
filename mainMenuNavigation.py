import mainMenu
import searchFlights
import login
import authentication
import userRegistration

def mainMenuNavigation(mainMenuChoice):
    
    while mainMenuChoice != 4:

        ########## SEARCH UPCOMING FLIGHTS ##########
        if mainMenuChoice == 1:
            print("Navigating to Search Portal...")
            print()
            searchChoice = searchFlights.searchFlightsMenu()
            
            while(searchChoice.lower() != "c"):
                
                if searchChoice.lower() == "a":
                    searchFlights.searchByDepartureArrivalDestination()
                    searchChoice = searchFlights.searchFlightsMenu()
                
                elif searchChoice.lower() == "b":
                    searchFlights.searchByDate()
                    searchChoice = searchFlights.searchFlightsMenu()
                
                else:
                    print("Wrong option entered")
                    searchChoice = searchFlights.searchFlightsMenu()
            
            if(searchChoice.lower() == "c"):
                print("Navigating back to main menu...")
                mainMenuChoice = mainMenu.mainMenuDisplay()


        ########## LOGIN ##########
        elif mainMenuChoice == 2:
            print("Navigating to Login Portal...")
            print()
            loginDetails = login.loginDetails()

            while(loginDetails[2].lower() !="c"):

                #### CUSTOMER ####
                if loginDetails[2] == "a":
                    custAuthResult = authentication.authenticateCustomer(loginDetails[0],loginDetails[1])
                    custAuth = custAuthResult[0]
                    custDetails = custAuthResult[1]
                    
                    if(custAuth):
                        login.customerLoginWelcome(custDetails)
                        customerChoice = login.customerLoginMenu()

                    while(custAuth and customerChoice.lower() != "f"):
                        if customerChoice.lower() == "a":
                            login.customerMakeBooking(custDetails)
                            customerChoice = login.customerLoginMenu()
                            
                        elif customerChoice.lower() == "b":
                            login.customerCancelBooking(custDetails)
                            customerChoice = login.customerLoginMenu()

                        elif customerChoice.lower() == "c":
                            login.updateCustomerDetails(custDetails)
                            customerChoice = login.customerLoginMenu()
                        
                        elif customerChoice.lower() == "d":
                            login.viewCustomerBookings(custDetails)
                            customerChoice = login.customerLoginMenu()

                        elif customerChoice.lower() == "e":
                            login.viewCustomerDetails(custDetails)
                            customerChoice = login.customerLoginMenu()
                        
                        else:
                            print("Wrong option entered")
                            print()
                            customerChoice = login.customerLoginMenu()

                    if(custAuth and customerChoice.lower() == "f"):
                        print("Navigating back to Main Menu...")
                        mainMenuChoice = mainMenu.mainMenuDisplay()
                        break
                    else:
                        print("Invalid login details!")
                        print("Navigating back to Main Menu...")
                        mainMenuChoice = mainMenu.mainMenuDisplay()
                        break

                #### STAFF ####
                elif loginDetails[2].lower() == "b":
                    staffAuthResult = authentication.authenticateStaff(loginDetails[0],loginDetails[1])
                    staffAuth = staffAuthResult[0]
                    staffDetails = staffAuthResult[1]

                    if(staffAuth):
                        login.staffLoginWelcome(staffDetails)
                        staffChoice = login.staffLoginMenu()

                    while(staffAuth and staffChoice.lower() != "f"):
                        if staffChoice.lower() == "a":
                            login.staffViewFlights()
                            staffChoice = login.staffLoginMenu()
                            
                        elif staffChoice.lower() == "b":
                            login.staffAddFlights()
                            staffChoice = login.staffLoginMenu()

                        elif staffChoice.lower() == "c":
                            login.staffChangeFlightStatus()
                            staffChoice = login.staffLoginMenu()
                        
                        elif staffChoice.lower() == "d":
                            login.updateStaffDetails(staffDetails)
                            staffChoice = login.staffLoginMenu()

                        elif staffChoice.lower() == "e":
                            login.viewStaffDetails(staffDetails)
                            staffChoice = login.staffLoginMenu()
                        
                        else:
                            print("Wrong option entered")
                            print()
                            staffChoice = login.staffLoginMenu()

                    if(staffAuth and staffChoice.lower() == "f"):
                        print("Navigating back to Main Menu...")
                        mainMenuChoice = mainMenu.mainMenuDisplay()
                        break
                    else:
                        print("Invalid login details!")
                        print("Navigating back to Main Menu...")
                        mainMenuChoice = mainMenu.mainMenuDisplay()
                        break

                else:
                    print("Wrong option entered")
                    loginDetails = login.loginDetails()
            
            if loginDetails[2].lower() =="c":
                print()
                print("Navigating back to Main Menu...")
                mainMenuChoice = mainMenu.mainMenuDisplay()
                  

        ########## NEW USER REGISTERATION ##########
        elif mainMenuChoice == 3:
            print("Navigating to Registeration Portal...")
            print()
            registerChoice = userRegistration.userRegistrationMenu()

            while(registerChoice.lower() != "c"):
                
                if registerChoice.lower() == "a":
                    userRegistration.newCustomerRegisteration()
                    registerChoice = userRegistration.userRegistrationMenu()
                
                elif registerChoice.lower() == "b":
                    userRegistration.newStaffRegisteration()
                    registerChoice = userRegistration.userRegistrationMenu()
                
                else:
                    print("Wrong option entered")
                    registerChoice = userRegistration.userRegistrationMenu()
            
            if(registerChoice.lower() == "c"):
                print("Navigating back to main menu...")
                mainMenuChoice = mainMenu.mainMenuDisplay()

            
        else:
            print("Wrong option entered")
            mainMenuChoice = mainMenu.mainMenuDisplay()

    if mainMenuChoice == 4:
        print("---------------------------------------------------------------------")
        print("THANK YOU FOR VISITING US! SEE YOU SOON :) ")
        print("---------------------------------------------------------------------")
