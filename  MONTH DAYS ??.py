month=int(input("Please enter the month number : "))
if month<13:
    if month==2:
       year=int(input("Year:"))
       if year%4==0 and year%100==0 and year%400 :
         print("The number of days are 29")
       else:
         print("The number of days are 28")  
    elif month>=8:
       if month%2==0:
        print("The number of days are 31")
       else:
        print("The number of days are 30") 
    elif month%2==0:
        print("The number of days are 30")      
    else:
        print("The number of days are 31")         
else:
    print("Only 1-12 expected")    