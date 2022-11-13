import mysql.connector as mysql
import os
from dotenv import load_dotenv
import random
import time
import string 

load_dotenv()
def startUp():
    # Start MYSQL connection
    PASSWORD = os.getenv('PASSWORD')
    USER = os.getenv('USER')
    DB = os.getenv('DATABASE')

    connection = mysql.connect(host='localhost', user=USER, password=PASSWORD, database=DB) #Connection Object
    cursor = connection.cursor()
    if(connection.is_connected() == False):
        print("[-] Please give in the correct credentials.")

    cursor.execute("CREATE TABLE IF NOT EXISTS movies (id int, name VARCHAR(255), phone int, email VARCHAR(255), count int)")
    return cursor, connection

def DisplayMovies():#to display the list of movies available
        movieList = ["1:Black Panther: Wakanda Forever","2:The Batman","3:Bullet Train","4:Nope","5:RRR","6:Top Gun: Mavric",
                     "7:Jurassic World: Dominion","8:Doctor Strange in The Multiverse of Madness","9:KGF:Chapter 2","10:Minions: The Rise of Gru"]
       
        for i in range(10):
            print(movieList[i])
        choice = int(input("Enter your choice:"))
        movieChosen = movieList[choice-1]
        return movieChosen
 #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
 
def MovieInfo(movieChosen): #to display the information of the movie chosen
        movieInfo = {"1:Black Panther: Wakanda Forever":"description",
                     "2:The Batman":"description",
                     "3:Bullet Train":"description",
                     "4:Nope":"description",
                     "5:RRR":"description",
                     "6:Top Gun: Mavric":"description",
                     "7:Jurassic World: Dominion":"description",
                     "8:Doctor Strange in The Multiverse of Madness":"description",
                     "9:KGF:Chapter 2":"description",
                     "10:Minions: The Rise of Gru":"description"}
        print(movieChosen)
        print("Description:",movieInfo[movieChosen])
 #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
 
def Theaters():#to display the theaters where the movie is being screened  
              #and ""return the timings choosen""variable- show_time, theater details - theaterD
        theaterList = ["1)PVR:Vega City, Bannerghatta","2)Cinepolis:Royal Meenakshi Mall","3)INOX:Central,JP Nagar",
                            "4)PVR:Nexus(Forum),Kormangala"]
        for i in range(4):
            print("~",theaterList[i])
        choice = int(input("Enter your choice:"))
        theatername = theaterList[choice-1]
        return theatername
               
 #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
 
def Seats(): #to display the availability of seats(theater seats)
    arrP = []
    rowP,colmP = (3,10)
    p = 1
    for i in range(rowP):
        col = []
        for j in range (colmP):
            col.append(p)
            p+=1
        arrP.append(col)
    print()
    print("--------------------------------------------")
    print("PRIME:Rs.550")
    for i in range(-1,-len(arrP)-1,-1) :
        print("|",arrP[i],"|")
    print()  
    row,colm = (10,10)
    a = 1
    for i in range(row):
        col = []
        for j in range(colm):
            col.append(a)
            a+=1
        arr.append(col)
    print("CLASSIC:Rs.250")
    for i in range(-1,-len(arr)-1,-1) :
        print("|",arr[i],"|")
    print()
    print()
    print()
    print("  ============SCREEN=====================")
    choice = input("enter your choice, CLASSIC or PRIME:")
    choice = choice.strip()
    choice = choice.upper()
    if choice == "PRIME":
        print("~The Tickets have sold out, you can try to book your tickets in CLASSIC")
    elif choice == "CLASSIC":
        print("Lets choose the seats")
 #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
 
def RangeOfTheSeat(seatNoX):  # Extracts the seat index and sends it to Primary_array() function
    if seatNoX in range(1,11): #index is in the range [0,9]
            seatIndex = seatNoX-1            
            extList = [0]
            extList.append(seatIndex)
            a = int(extList[0])
            b = int(extList[1])
            Primary_array(a,b)
    elif seatNoX in range(11,101): #Index is in the range [10,99]
            seatIndex = str(seatNoX-1)
            extList = list(seatIndex)
            a = int(extList[0])
            b = int(extList[1])
            Primary_array(a,b)
 
 #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
 
def Sellect_seat(): # Seat selection module
    print()
    noOFseats = int(input("Enter the number of seats(can select max 5):"))
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    if noOFseats == 1:
        temp =  int(input("Enter the seat number"))
        seatNo.append(temp)
        seatNo1 = int(seatNo[0])
        RangeOfTheSeat(seatNo1)                                            
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    elif noOFseats == 2:
        temp = eval(input("Enter the First Seat number:"))
        seatNo.append(temp)
        temp = eval(input("Enter the Second Seat number:"))
        seatNo.append(temp)
        seatNo1 = seatNo[0]
        seatNo2 = seatNo[1]
        RangeOfTheSeat(seatNo1)
        #\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
        RangeOfTheSeat(seatNo2)
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    elif noOFseats == 3:
        #seatNo = []  # This is a global variable, which will already be initiallised, so this line will be omitted in the main program
        temp = eval(input("Enter the First Seat number:"))
        seatNo.append(temp)
        temp = eval(input("Enter the Second Seat number:"))
        seatNo.append(temp)
        temp = eval(input("Enter the Third Seat number:"))
        seatNo.append(temp)
        seatNo1 = seatNo[0]
        seatNo2 = seatNo[1]
        seatNo3 = seatNo[2]
        RangeOfTheSeat(seatNo1)
        #\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
        RangeOfTheSeat(seatNo2)
        #\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
        RangeOfTheSeat(seatNo3)
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    elif noOFseats == 4:
        temp = eval(input("Enter the First Seat number:"))
        seatNo.append(temp)
        temp = eval(input("Enter the Second Seat number:"))
        seatNo.append(temp)
        temp = eval(input("Enter the Third Seat number:"))
        seatNo.append(temp)
        temp = eval(input("Enter the Forth Seat number:"))
        seatNo.append(temp)
        seatNo1 = seatNo[0]
        seatNo2 = seatNo[1]
        seatNo3 = seatNo[2]
        seatNo4 = seatNo[3]
        RangeOfTheSeat(seatNo1)
        #\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
        RangeOfTheSeat(seatNo2)
        #\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
        RangeOfTheSeat(seatNo3)
        #\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
        RangeOfTheSeat(seatNo4)
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    elif noOFseats == 5:
        temp = eval(input("Enter the First Seat number:"))
        seatNo.append(temp)
        temp = eval(input("Enter the Second Seat number:"))
        seatNo.append(temp)
        temp = eval(input("Enter the Third Seat number:"))
        seatNo.append(temp)
        temp = eval(input("Enter the Forth Seat number:"))
        seatNo.append(temp)
        temp = eval(input("Enter the Fifth Seat number:"))
        seatNo.append(temp)
        seatNo1 = seatNo[0]
        seatNo2 = seatNo[1]
        seatNo3 = seatNo[2]
        seatNo4 = seatNo[3]
        seatNo5 = seatNo[4]
        RangeOfTheSeat(seatNo1)
        #\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
        RangeOfTheSeat(seatNo2)
        #\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
        RangeOfTheSeat(seatNo3)
        #\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
        RangeOfTheSeat(seatNo4)
        #\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
        RangeOfTheSeat(seatNo5)
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
 
 
    elif noOFseats == 0:
        print("you cannot select zero seats")#if seates is zero it should come out of the function
                                             #i still need to think of the waf to do so
                                             #most likely i will return zero, which signifies that the user doesnot want to book the tickets
                                             #NOT COMPLETED
    elif noOFseats>100:
        print("~~Classic section has a seating capacity of only 100 people")
        print("~~Enter 0 if u want to cancel ticket booking OR enter -1 if u want to reatart the booking")#NOT COMPLETED
 #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
 
def Primary_array(a,b):# fills the seat in the theater
    arr[a][b]="F"
 #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
 
def Amount(n_seates):# To display the final amount of the movie
       try:
           amount = n_seates*250
           gst = (0.18*amount)
           convenience_fee = gst+60
           f_amount = amount+gst+60
           print("Ticket price=",amount,"\nconvenience_fee=",convenience_fee)
           print()
           print("Before proceeding to pay we would like you to fill some personal details for security reasons: ")

           print("Total Payable Amount:",f_amount)
       except:
           print("[-] There was some unexcepted error. Please try again!")
 #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
 
def UserDetails(cursor, connection):  #To accept the user details and store it in the database
        name = input("Enter your name: ")
        email = input("Enter your email: ")
        phone = input("Enter your phone number: ")
        count = 1
        cursor.execute("SELECT * FROM movies WHERE email = %s", (email,))
        data = cursor.fetchone()
        if cursor.rowcount >= 1:
            count = data[4] +1
            cursor.execute("UPDATE movies SET count = %s WHERE email = %s", (count, email))
            connection.commit()
        else:
            cursor.execute("INSERT INTO movies (id, name, email, phone,count) VALUES (%s, %s, %s,%s,%s)", (random.randint(1000, 10000),name, email, phone,count))
            connection.commit()

        print("[+] Thank You for choosing us! Your ticket has been booked successfully.Please check your email for a confirmation message.")

 #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
 
def Payment():# to accept the payment
       try:
           print()
           print("enter 1 for UPI else enter 2 for card ")
           choice = int(input("Enter your choice 1 or 2:"))
           if choice==1:
                id_upi = input("enter UPI ID")
                print("\rProcessing.......")
                time.sleep(random.randint(0,5))
                print("\rPayment sucessful")
           elif choice == 2:
                cardD = input("Enter Card Number")
                print("\rProcessing.......")
                time.sleep(random.randint(0,5))
                print("\rPayment sucessful")
           return ''.join(random.choices(string.ascii_uppercase + string.digits, k = 10))    
       except:
           print("[-] There was some unexcepted error. Please try again!")
 #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
 
def Tickets(orderID,theaterName,movie_name): #To print the ticket
    print()
    print("~"*100)
    print("Your ticket")
    print()
    print("Order ID:",orderID)
    print("(3D)",movie_name)
    print("ENGLISH WITH ENGLISH SUBTITLES\n(IMAX)\nENGLISD (U/A)")
    print("~"*100)
    print(theaterName)
    print("AUDI 02 ")
    for i in range(len(seatNo)):
        print(seatNo[i], end=",")
    print("~"*100)
    print()
 #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
 
           
# Invoke the functions

if __name__ == "__main__":
    arr = []
    seatNo = []
    print("~ WELCOME TO MOVIE TICKET BOOKING SERVICE ~")
    print()
    print("Here are the list of movies currently airing ~")
    movie_Chosen = DisplayMovies()
    MovieInfo(movie_Chosen)
    print()
    print("Do you wish to proceed ?")
    print('\n')
    print('If yes then enter "1"\nElse enter "0" to display the movie list again')
    choice1 = int(input("Enter your choice: "))
    if choice1 == 0:
        movie_Chosen = DisplayMovies()
        MovieInfo(movie_Chosen)
    elif choice1 == 1:
        print("Processing...")
    else:
        print("Invalid input")
    print('\n')
    print("Lets choose the theater of your choice")
    theaterName = Theaters()
    Seats()
    Sellect_seat()
    n_seates = len(seatNo)
    Amount(n_seates)
    orderID = Payment()
    cursor , connection = startUp()
    UserDetails(cursor, connection) # Get the user details and store them.
    Tickets(orderID,theaterName,movie_Chosen) # Print the ticket
    

 
