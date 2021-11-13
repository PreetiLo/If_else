print ( " *Welcome to Pune Bank " )
print ( " Please swipe your atm card " )
balance = 5000000
lang = input ( " Which language do you prefer ? " )
if lang == "english" or lang == "ENGLISH" or lang == "English" :
    PIN = int ( input ( " Enter your PIN number : " ) )
    if PIN>=1 and PIN<=9  :
        print ( " Correct PIN number. " )
        trans = input ( " Enter the type of transaction ( Please enter number from 1-6 ) : " )
        if trans == "1" :
            print ( " 1. Balance enquiry " )
            slip = input ( "Do you want a receipt of your account balance? (yes or no): " )
            if slip == "yes" :  
                print ( "Here is your receipt. Please collect it. Thanks for using Pune Bank! " 
                if trans == "2" :
                    print ( " 2. Cash withdrawal " )
                    AMT = int ( input ( " Enter the amount to be collected. " ) )
                    print ( " Please collect your cash. " )
                    if trans == "3"  : 
                        print ( " 3. deposite money " ) 
                        amt = int ( input ( " Enter then amount to be deposited. " ) )
                        print ( " Your money has been successfully deposited. " )     
                        if trans == "4" :
                            print ( " 4. Change your pin " )
                            PIN_1 = int ( input ( " Enter old PIN number : " ) )
                            if PIN == PIN_1 :
                                PIN_2 = int ( input ( " Enter new PIN number : " ) )
                                print ( " Your PIN has been successfully changed. " )
                                if trans == "5" :
                                    print ( " 5. transfer money " )
                                    Amt = int (input ( "Enter the amount of money you wish to transfer:" ) )
                                    if Amt > 0 :
                                        print ( " Your amount has been successfully transferred. " )
                                        if trans == "6" :
                                            print ( " Quit " )
                                        else:
                                            print ( " False " )
                                    else:
                                        print ( " Please enter an appropriate amount." )
                                else: 
                                    print ( " ERROR " )
                            else:
                                print ( " Incorrect PIN number. Please retry. " ) 
                        else:
                            print ( " ERROR " )                       
                    else :
                        print ( " Incorrect amount. Please retry. " )
                else:
                    print ( " ERROR " )
            else:
                print ( " Thank you ! " )
        else:
            print ( " ERROR " )
    else:
        print ( " Incorrect PIN number. Please retry. " )
else :
    print ( " This language is unavailable " )                