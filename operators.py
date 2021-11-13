a=int(input("enter a number"))
b=int(input("enter another number"))
opr= input("enter any operator:")
if opr=="+" or opr=="addition":
    print(a+b)
elif opr=="-" or opr=="subtraction":
    print(a-b)
elif opr=="*" or opr=="multiplication":
    print(a*b)
elif opr=="/" or opr=="division":
    print(a/b)
elif opr=="%" or opr=="modulus":
    print(a%b)
elif opr=="**" or opr=="exponentiation":
    print(a**b)
elif opr=="//" or opr=="floor division":
    print(a//b)
else:
    print("please enter an appropriate operator.")