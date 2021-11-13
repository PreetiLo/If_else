no_h=int(input("enter number of classes held:"))
no_a=int(input("enter number of classes attended:"))
attend=(no_a/no_h)*100 
if attend>=75:
    print("you are allowed to sit in the exam")
else:
    print("you are not allowed to sit in the exam")