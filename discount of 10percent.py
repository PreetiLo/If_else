quantity=input("enter quantity")
if quantity*100>1000:
    print("the cost is" ,quantity*100-0.1*quantity*100)
else:
    print("the cost is",quantity*100)
