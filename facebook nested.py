name=input("What is your name? " )
surname= input("What is your surname: ")
if name=="preeti" and surname=="kumari":
    print("full name ",name,surname)
    # surname= input("What is your surname: ") 
    # if surname=="kumari":
        # print (surname)
    birthdate=input("What is your birthdate") 
    if birthdate=="10/07/1997":
        print("Your birthdate is ",birthdate) 
        gender=input("What is your gender")
        if gender =="Female":
            print(gender)
            mobile=int(input("Enter your mobile number or e-malil id:"))
            email=input("enter the email i'd") 
            if mobile == 8368987896 :
                print("Mobile number is", mobile)
                if email=="preetikumarijuly10@gmail.com": 
                    print("Mobile number is", mobile,email)
                    password=int(input("Enter your password")) 
                    if password==2211:
                        print("password")
                    else:
                        print("wrong password try again")
                else:
                    print("Incorrect mobile number")
            else:
                print("not in option")
        else:
            print("wrong birthdate try again")
    else:
        print("wrong surname try again")
else:
    print("wrong name try again")