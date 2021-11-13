print (" * Welcome to Pune Bank * ")
print ("Please swipe your card")
pin_inp = 3635
pin = int ( input ( "Please enter your pin number : " ) )
if pin == 3635 :
    print ( "1. Balance enquiry" ) 
    print ( "2. Withdraw money" )
    print ( "3. deposite money" )
    print ( "4. Change your pin" )
    print ( "5. transfer money" )
    print ( "6. Quit" )
    trans = input ( "Enter the mode of transaction ( Please select the number ) :" )
    if trans == "1":
        slip = input ( "Do you want a receipt (yes or no): " )
        if slip == "yes":
            print ( "Here is your receipt. Please collect it. Thanks for using Pune Bank! " )
        else:
            print ( "Thankyou for using Pune Bank! " )
    elif trans == "2":
        amt = int ( input ( "Enter the amount of money you wish to withdraw: " ) )
        if amt > 0 :
            print ( "Please collect your cash. Thank you for using Pune Bank!" )
        else:
            print ( "Please enter a valid amount to proceed." ) 
    elif trans == "3":
        AMT = int ( input ( "Enter the amount which you wish to deposite : " ) )
        if AMT > 0 :
            print ( "Your money has been successfully deposited." )
        else:   
            print ( "Enter valid amount of deposite." )   
    elif trans == "4" :
            pin_1 = int ( input ( "Enter the old pin : " ) )
            if pin_1 == pin_inp: 
                pin_2 = int ( input ( "Enter new pin:" ) )
                print ( "Your new pin has been successfully updated." )
            else:
                print ( "Please enter the valid old pin." )
    elif trans == "5":
            Amt = int (input ( "Enter the amount of money you wish to transfer:" ) )
            if Amt > 0 :
                print ( "Your amount has been successfully transferred." )
            else:
                print ( "Please enter an appropriate amount." )
    elif trans == "6":
                print ( "Quit" )                
    else:
        print ( "Please choose any transaction mode." )
else:
    print ( "Please enter a valid pin. " )