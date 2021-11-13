a = int(input("enter first number : "))
b = int(input("enter second number : "))
c = int(input("enter third number : "))
if a<b :
    print("a is the minimum number")
    if a<c :
        print("a is the minimum number")
        if b<a :
            print("b is the minimum number")
            if b<c :
                print("b is the minimum number")
            else:
                print("c is the minimum number")
        else:
            print("a is the minimum number")
    else:
        print("c is the minimum number")
else :
    print("b is the minimum number")