#Ronil Soto Baez
#Monday 2,2016
#Airline Flight Scheduling

#--------------------------------------------------------------------------------------------------------------------------------------------

# this funtion read the lists of the flights
# and separate into five diferrents list to work with.
def getLists():
    
    fileName = 'flights.txt'
    inFile = open(fileName,'r')
    airlineList=[]
    flightNumberList=[]
    departureTimeList=[]
    arrivalTimeList=[]
    priceList=[]
    line = inFile.readline()
    while line!="":
        line = line.strip()
        airline,flightNumber,departureTime,arrivalTime,price= line.split(",")
        airlineList=airlineList+[airline]
        flightNumberList=flightNumberList+[flightNumber]
        departureTimeList=departureTimeList+[departureTime]
        arrivalTimeList=arrivalTimeList+[arrivalTime]
        priceList=priceList+[price]
        line = inFile.readline()
    return airlineList,flightNumberList,departureTimeList,arrivalTimeList,priceList
    inFile.close()
#--------------------------------------------------------------------------------------------------------------------------------------------

    
  # This funtion display the main menu.      
def Display():
    print('Please choose one of the following options:')
    print('1 -- Find all flights on a particular airline')
    print('2 -- Find the cheapest flight')
    print('3 -- Find all the flights less than a specified price')
    print('4 -- Find the shortest flight')
    print('5 -- Find all flights that depart within a specifed range')
    print('6 -- Find the average price for a specified airline')
    print('7 -- Quit')
 #--------------------------------------------------------------------------------------------------------------------------------------------

    
#Prompt the user for the name of the airline
#if the input is not valir, ask again
#prompt the user for the name of the airline again
#displays for the user all flights on a particular airline
def findParticularAirline(airlineList,flightNumberList,departureTimeList,arrivalTimeList,priceList):
    
    found=False
    airline=input('Enter the name of the airline: ')
    for i in range (len(airlineList)):
        if (airlineList[i]==airline):
            found=True
    if found==False:
            print('Invalid input -- please try again')
            findParticularAirline(airlineList,flightNumberList,departureTimeList,arrivalTimeList,priceList)
    if (found==True):
        print('')
        print('AIRLINE   FLT#   DEPT    ARR   PRICE')
        print('--------------------------------------------------------')
        for i in range (len(airlineList)):
            if (airlineList[i]==airline):
                print(airlineList[i]," ",flightNumberList[i],'\t',departureTimeList[i],'\t',arrivalTimeList[i],'\t',priceList[i])
#--------------------------------------------------------------------------------------------------------------------------------------------

                

#Display the flight that has the lowest cost   
def findCheapestFlight(airlineList,priceList):
    
    cheapestPrice=priceList[0]
    for i in range (len(airlineList)):
        if cheapestPrice>=priceList[i]:
            cheapestPrice=priceList[i]
            airline=airlineList[i]
    return cheapestPrice,airline
#--------------------------------------------------------------------------------------------------------------------------------------------


#promt the user the maximum price and then print
#the flight information for each of the flights whose price is less than that maximum.
def findFlightsLessThan(cheapestPrice,airlineList,flightNumberList,departureTimeList,arrivalTimeList,priceList):
    
    maxPrice='$'+input('Enter your maximum price: $')
    if (maxPrice<cheapestPrice):
            print ('no flights meet your criteria.')
     
    else:
        print('')
        print('AIRLINE    FLT#  DEPT  ARR    PRICE')
        print('--------------------------------------------------------')
        for i in range (len(airlineList)):
            if (priceList[i]<maxPrice):
                if len(airlineList[i])>6:
                  print(airlineList[i],'',flightNumberList[i],'\t',departureTimeList[i],'\t',arrivalTimeList[i],'\t',priceList[i])
                else:
                    print(airlineList[i],'\t',flightNumberList[i],'\t',departureTimeList[i],'\t',arrivalTimeList[i],'\t',priceList[i])
#--------------------------------------------------------------------------------------------------------------------------------------------

#Display the flight with the shortest duration                  
def findShortestFlight(airlineList,flightNumberList,departureTimeList,arrivalTimeList):
    
    flightDuration=[]
    for i in range(len(departureTimeList)):
    
        deptHours,deptMinutes=departureTimeList[i].split(':')
        arrHours,arrMinutes=arrivalTimeList[i].split(':')
        deptHoursToMinutes=int(deptHours)*60
        arrHoursToMinutes=int(arrHours)*60
        deptTotal=deptHoursToMinutes+(int(deptMinutes))
        arrTotal=arrHoursToMinutes+(int(arrMinutes))
        flightDuration=flightDuration+[arrTotal-deptTotal]
    shortestDuration=flightDuration[0]
    
    for i in range(len(departureTimeList)):
        if shortestDuration>flightDuration[i]:
            shortestDuration=flightDuration[i]
            index=i
    print('')
    print('The shortest flight is in ',airlineList[index],flightNumberList[index],'at ',shortestDuration,"minutes")
#--------------------------------------------------------------------------------------------------------------------------------------------

    
#promt the user for the earliest allowable departure time ask again if is not correct
#promt the user for the latest allowable departure time ask again if is not correct
# display the time that meet the criteria
#if no time meet the criteria display no flights meet this criteria        
def findTimeRange(airlineList,flightNumberList,departureTimeList,arrivalTimeList,priceList):
    
    timeRangeIndex=[]
    earliestTime=input('Enter the earliest allowable departure time')
    found = False
    for i in range (len(airlineList)):
        if (departureTimeList[i]==earliestTime):
            found=True
    if found==False:
            print('Invalid time -- please try again')
            findTimeRange(airlineList,flightNumberList,departureTimeList,arrivalTimeList,priceList)
        
    if (found==True):
        latestTime=input('Enter the latest allowable departure time')
        found=False
        for i in range (len(airlineList)):
            if (departureTimeList[i]==latestTime):
                found=True
    if found==False:
            print('Invalid time -- please try again')
            findTimeRange(airlineList,flightNumberList,departureTimeList,arrivalTimeList,priceList)
    if (found==True):

        print('')
        print('AIRLINE  FLT#    DEPT    ARR     PRICE')
        print('--------------------------------------------------------')
        for i in range(len(departureTimeList)):
            if earliestTime<=departureTimeList[i] and latestTime>=departureTimeList[i]:
                if len(airlineList[i])>6:
                      print(airlineList[i],'',flightNumberList[i],'\t',departureTimeList[i],'\t',arrivalTimeList[i],'\t',priceList[i])
                else:
                        print(airlineList[i],'\t',flightNumberList[i],'\t',departureTimeList[i],'\t',arrivalTimeList[i],'\t',priceList[i])

#------------------------------------------------------------------------------------------------------------------------------------------------------------


#prompt the user for the name of the airlinen and ask again if is not correct.
#Display the average price for flights for a given airline
#If the user enters a price that is lower than all of the prices, display no flights meet this criteria            
def findAvgPrice(priceList,airlineList):
    
    count=0
    totalPrice=0
    airlineName=input('Enter name of airline: ')
    found=False
    for i in range (len(airlineList)):
        if (airlineList[i]==airlineName):
            found=True
    if found==False:
            print('Invalid input -- please try again')
            findAvgPrice(priceList,airlineList)
    if (found==True):
        for i in range(len(airlineList)):
            if airlineName==airlineList[i]:
                price=priceList[i][1:]
                totalPrice+=int(price)
                count=count+1
        print('')
        print('The average price is $',totalPrice/count)
#--------------------------------------------------------------------------------------------------------------------------------------------

        
# This funtion is going to call the other funtions depending what the user choice is.
# and if the user choice is 7, exit the program
def main():

    airlineList,flightNumberList,departureTimeList,arrivalTimeList,priceList=getLists()
    cheapestPrice,airline=findCheapestFlight(airlineList,priceList)
    choice =0
    
    while (choice) < 7 and (choice>=0):
        print('')
        Display()
        choice =int(input('Choise==> '))
        if choice ==1:
            findParticularAirline(airlineList,flightNumberList,departureTimeList,arrivalTimeList,priceList)
            
        if choice ==2:
            findCheapestFlight(airlineList,priceList)
            print('The cheapest flight is in ',airline,'at ',cheapestPrice)
            
        if choice==3:
            findFlightsLessThan(cheapestPrice,airlineList,flightNumberList,departureTimeList,arrivalTimeList,priceList)
            
        if choice==4:
            findShortestFlight(airlineList,flightNumberList,departureTimeList,arrivalTimeList)
           
        if choice==5:
            findTimeRange(airlineList,flightNumberList,departureTimeList,arrivalTimeList,priceList)
            
        if choice==6:
            findAvgPrice(priceList,airlineList)
            
    if choice==7:
            print('thank you')
            return
