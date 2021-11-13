user1=int(input("Enter first number"))
user2=int(input("Enter second number"))
user3=int(input("Enter third number"))
if(user1>user2 and user1>user3):
    print("First number is greater")
elif(user2>user1 and user2>user3):
    print("Second number is greater")
elif(user3>user2 and user3>user1):
    print("third number is greater") 
else:
    print("no number")