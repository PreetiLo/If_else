age1=int(input("enter the age of first person:"))
age2=int(input("enter the age of second person:"))
age3=int(input("enter the age of third person:"))
if age1>age2 and age1>age3:
    print("first person is the oldest one.")
elif age2>age1 and age2>age3:
    print("second person is the oldest one.")
elif age3>age1 and age3>age2:
    print("third peron is the oldest one.")
else:
    print("all are of equal ages.")