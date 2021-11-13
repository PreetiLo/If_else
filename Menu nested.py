day=input("What is the day today?")
time=input("Enter the time at which you wish to cook the meal (breakfast, dinner or lunch):")
if (day == "monday"):
    if(time == "dinner"):
       print("rice")
    elif (time =="lunch"): 
        print("daal roti")
    else:
        print("poha")
elif (day == "tuesday"):
    if (time == "lunch"):
        print("paneer")
    elif (time == "dinner"):
        print ("Pav-Bhaji")
    else:
        print("omlet")
elif (day == "wednesday"):
    if (time == "lunch"):
        print ("palak gobi")
    elif (time == "dinner"):
        print ("shimla mirch")
    else:
        print("idli chutney")
elif (day == "thursday"):
    if (time == "lunch"):
        print ("bhindi")
    elif (time == "dinner"):
        print ("chhole bhature")
    else:
        print("misal paav")
elif (day == "friday"):
    if (time == "lunch"):
        print ("manchurian")
    elif (time == "dinner"):
        print ("pizza")
    else:
        print("dosa")
elif (day == "saturday"):
    if (time == "lunch"):
        print ("pasta")
    elif (time == "dinner"):
        print ("brinjal")
elif (day== "sunday"):       
    if (time == "lunch"):
        print ("aloo matar")
    elif (time == "dinner"):    
        print ("veg pulav")
    else:
        print("dhokla")
else:
        print ("ERROR")