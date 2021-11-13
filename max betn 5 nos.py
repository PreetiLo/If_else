user1=int(input("enter the first number:"))
user2=int(input("enter the second number:"))
user3=int(input("enter the third number:"))
user4=int(input("enter the fourth number:"))
user5=int(input("enter the fifth number:"))
if user1>user2 and user1>user3 and user1>user4 and user1>user5:
    print("first number is the greatest")
elif user2>user1 and user2>user3 and user2>user4 and user2>user5:
    print("second number is the greatest")
elif user3>user1 and user3>user2 and user3>user4 and user3>user5:
    print("third number is the greatest")
elif user4>user1 and user4>user2 and user4>user3 and user4>user5:
    print("fourth number is the greatest")
elif user5>user1 and user5>user2 and user5>user3 and user5>user4:
    print("fifth number is the greatest")
else:
    print("all numbers are equal")