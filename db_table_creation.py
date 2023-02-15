import mysql.connector


def createDatabase():
    mydb = mysql.connector.connect(host="localhost", user="root", password="root")
    mycursor = mydb.cursor()

    #### CREATE DATABASE ####
    mycursor.execute("DROP DATABASE IF EXISTS Project_Varuni")
    mycursor.execute("CREATE DATABASE IF NOT EXISTS Project_Varuni")
    mycursor.execute("USE Project_Varuni")
    mycursor = mydb.cursor()

    #### CREATE TABLE AIRLINE ####
    mycursor.execute('''CREATE TABLE IF NOT EXISTS AIRLINE(
                                AirlineID INT(5) PRIMARY KEY,
                                AirlineName CHAR(20),
                                Seats CHAR(3)
                        )''')

    sqlairline = 'INSERT INTO AIRLINE VALUES(%s,%s,%s)'
    valairline = [
        (14895, 'Emirates', '300'),
        (13486, 'Indigo', '300'),
        (17345, 'Air India', '300'),
        (23189, 'Singapore Airlines', '300')
    ]
    mycursor.executemany(sqlairline, valairline)
    mydb.commit()

    #### CREATE TABLE AIRPORT ####
    mycursor.execute('''CREATE TABLE IF NOT EXISTS AIRPORT(
                                AirportCity CHAR(50) PRIMARY KEY,
                                AirportName CHAR(50)
                        )''')

    sqlairport = 'INSERT INTO AIRPORT VALUES(%s,%s)'
    valairport = [
        ('Delhi', 'IGI Airport'),
        ('Dubai', 'Dubai Airport'),
        ('Singapore', 'Changi Airport')
    ]
    mycursor.executemany(sqlairport, valairport)
    mydb.commit()

    #### CREATE TABLE FLIGHT ####
    mycursor.execute('''CREATE TABLE IF NOT EXISTS FLIGHT(
                                FlightNo CHAR(5) PRIMARY KEY,
                                DepartureAirport CHAR(50),
                                DepartureDate DATE,
                                DepartureTime TIME,
                                ArrivalAirport CHAR(50),
                                ArrivalDate DATE,
                                ArrivalTime TIME,
                                FlightStatus CHAR(10),
                                AirlineID INT,
                                Price_Child_Economy CHAR(10),
                                Price_Child_Business CHAR(10),
                                Price_Adult_Economy CHAR(10),
                                Price_Adult_Business CHAR(10),
                                Price_Senior_Economy CHAR(10),
                                Price_Senior_Business CHAR(10)
                        )''')

    sqlflight = 'INSERT INTO FLIGHT VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
    valflight = [
        ('10000', 'Dubai Airport', '2020-11-01', '19:30:00', 'IGI Airport', '2020-11-01', '22:30:00','ON TIME', "14895", "1000", "3000", "2000", "4000", "1000", "3000"),
        ('11000', 'Dubai Airport', '2020-11-02', '11:30:00', 'IGI Airport', '2020-11-02','14:30:00', 'EARLY', "13486", "1500", "3500", "2500", "4500", "1500", "3500"),
        ('12000', 'Dubai Airport', '2020-11-03', '09:30:00', 'IGI Airport', '2020-11-03', '12:30:00','ON TIME', "17345", "1200", "3200", "2200", "4200", "1200", "3200"),
        ('13000', 'Dubai Airport', '2020-12-01', '08:20:00', 'Changi Airport', '2020-12-01','14:20:00', 'EARLY', "14895", "2000", "4000", "3000", "5000", "2000", "4000"),
        ('14000', 'Dubai Airport', '2020-12-02', '10:30:00', 'Changi Airport', '2020-12-02','16:30:00', 'ON TIME', "13486", "1600", "3600", "2600", "4600", "1600", "3600"),
        ('15000', 'Dubai Airport', '2020-12-03', '13:10:00', 'Changi Airport', '2020-12-03','19:10:00', 'ON TIME', "23189", "1700", "3700", "2700", "4700", "1700", "3700"),
        ('16000', 'IGI Airport', '2020-11-04', '20:30:00', 'Dubai Airport', '2020-11-04', '22:30:00','ON TIME', "14895", "4000", "6000", "5000", "7000", "4000", "6000"),
        ('17000', 'IGI Airport', '2020-11-05', '19:30:00', 'Dubai Airport', '2020-11-05', '22:30:00','DELAYED', "17345", "1100", "3100", "2100", "4100", "1100", "3100"),
        ('18000', 'IGI Airport', '2020-11-06', '17:30:00', 'Dubai Airport', '2020-11-06', '20:30:00','ON TIME', "13486", "1000", "3200", "2200", "4200", "1200", "3200"),
        ('19000', 'IGI Airport', '2020-12-04', '19:30:00', 'Changi Airport', '2020-12-04','22:30:00', 'ON TIME', '14895', "1800", "3800", "2800", "4800", "1800", "3800"),
        ('20000', 'IGI Airport', '2020-12-05', '12:30:00', 'Changi Airport', '2020-12-05','15:30:00', 'ON TIME', "13486", "1900", "3900", "2900", "4900", "1900", "3900"),
        ('21000', 'IGI Airport', '2020-12-06', '11:30:00', 'Changi Airport', '2020-12-06','13:30:00', 'DELAYED', "23189", "1500", "3500", "2500", "4500", "1500", "3500"),
        ('22000', 'Changi Airport', '2020-11-11', '18:30:00', 'IGI Airport', '2020-11-11','20:30:00', 'ON TIME', "14895", "1000", "3000", "2000", "4000", "1000", "3000"),
        ('23000', 'Changi Airport', '2020-11-12', '06:30:00', 'IGI Airport', '2020-11-12','08:30:00', 'ON TIME', "13486", "2000", "4000", "3000", "5000", "2000", "4000"),
        ('24000', 'Changi Airport', '2020-11-13', '04:30:00', 'IGI Airport', '2020-11-13','06:30:00', 'DELAYED', "23189", "1000", "3000", "2000", "4000", "1000", "3000"),
        ('25000', 'Changi Airport', '2020-12-11', '04:30:00', 'Dubai Airport', '2020-12-11','10:30:00', 'ON TIME', "14895", "3000", "5000", "4000", "6000", "3000", "5000"),
        ('26000', 'Changi Airport', '2020-12-12', '11:30:00', 'Dubai Airport', '2020-12-12','17:30:00', 'ON TIME', "23189", "1000", "3000", "2000", "4000", "1000", "3000"),
        ('27000', 'Changi Airport', '2020-12-13', '10:30:00', 'Dubai Airport', '2020-12-13','16:30:00', 'ON TIME', "13486", "1000", "3000", "2000", "4000", "1000", "3000"),
    ]
    mycursor.executemany(sqlflight, valflight)
    mydb.commit()

    #### CREATE TABLE CUSTOMER ####
    mycursor.execute('''CREATE TABLE IF NOT EXISTS CUSTOMER(
                                CEmail CHAR(50) PRIMARY KEY,
                                CPassword CHAR(20),
                                CPassportNo CHAR(100),
                                CFirstName CHAR(50),
                                CLastName CHAR(50),
                                CDateOfBirth DATE,
                                CGender CHAR(10),
                                CPhoneNo CHAR(15),
                                CAddress CHAR(100),
                                CCity CHAR(20),
                                CCountry CHAR(20)
                        )''')

    sqlcustomer = 'INSERT INTO CUSTOMER VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
    valcustomer = [
        ('kajol@gmail.com', 'iamkajol', 'N1234567', 'Kajol', 'Devgan','1990-01-01', 'F', '050-3427784', 'Bandra-96', 'Mumbai', 'India'),
        ('srk@gmail.com', 'iamsrk', 'K1246567', 'ShahRukh', 'Khan','1970-11-25', 'M', '055-3427684', 'Bandra-09', 'Mumbai', 'India'),
        ('shraddha@gmail.com', 'iamshraddha', 'M6509235', 'Shraddha', 'Kapoor','1993-10-24', 'F', '050-8641256', 'Malad West-19', 'Mumbai', 'India')
    ]
    mycursor.executemany(sqlcustomer, valcustomer)
    mydb.commit()

    #### CREATE TABLE AIRLINE STAFF ####
    mycursor.execute('''CREATE TABLE IF NOT EXISTS AIRLINESTAFF(
                                SEMAIL CHAR(50) PRIMARY KEY,
                                SPassword CHAR(10),
                                SFirstName CHAR(50),
                                SLastName CHAR(50),
                                SDateOfBirth DATE,
                                SGender CHAR(10),
                                SPhoneNo CHAR(15)
                        )''')

    sqlstaff = 'INSERT INTO AIRLINESTAFF VALUES(%s,%s,%s,%s,%s,%s,%s)'
    valstaff = [
        ('manoj@gmail.com', 'manojcool', 'Manoj','Sharma', '1990-04-14', 'M', '050-7348924'),
        ('manvi@gmail.com', 'manvicool', 'Manvi','Kumar', '1989-07-29', 'F', '050-4545468')

    ]
    mycursor.executemany(sqlstaff, valstaff)
    mydb.commit()

    #### CREATE TABLE TICKET ####
    mycursor.execute('''CREATE TABLE IF NOT EXISTS TICKET(
                                TicketID CHAR(10) PRIMARY KEY,
                                AirlineName CHAR(20),
                                FlightNo CHAR(5),
                                TicketStatus CHAR(20),
                                CustomerEmail CHAR(50)
                        )''')

    sqlticket = 'INSERT INTO TICKET VALUES(%s,%s,%s,%s,%s)'
    valticket = [
        ('639548', 'Emirates', '11000', 'RESERVED', 'srk@gmail.com'),
        ('198456', 'Indigo', '15000', 'RESERVED', 'kajol@gmail.com'),
        ('281902', 'Air India', '21000', 'RESERVED', 'shraddha@gmail.com')

    ]
    mycursor.executemany(sqlticket, valticket)
    mydb.commit()

    #### CREATE TABLE PASSENGER_DETAILS ####
    mycursor.execute('''CREATE TABLE IF NOT EXISTS PASSENGER_DETAILS(
                                        PassengerID INT PRIMARY KEY AUTO_INCREMENT,
                                        PassengerFirstName CHAR(50),
                                        PassengerLastName CHAR(50),
                                        PassengerPassport CHAR(100) ,
                                        PassengerDOB DATE,
                                        PassengerAge CHAR(10),
                                        PassengerClass CHAR(10),
                                        TicketID CHAR(10)
                                )''')

    sqlpass = 'INSERT INTO PASSENGER_DETAILS VALUES(%s,%s,%s,%s,%s,%s,%s,%s)'
    valpass = [
        (100, 'Kajol', 'Devgan', 'N1234567','1990-01-01', '30', 'Business', '198456'),
        (101, 'ShahRukh', 'Khan', 'K1246567','1970-11-25', '50', 'Business', '639548')

    ]
    mycursor.executemany(sqlpass, valpass)
    mydb.commit()
