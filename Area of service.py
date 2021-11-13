age=input("Enter age")
sex=input("Enter sex. (M or F)")
marry=input("Married? (Y or N)")
if sex=="F":
    print("Urban areas only")
elif sex=="M" and age>=20 and age<=40:
    print("You can work anywhere") 
elif sex=="M" and age>40 and age<=60:
    print("Urban areas only")        
else:
    print("ERROR")    