ch=input("enter any character")
if ch>"a" and ch<"z" or ch>"A" and ch<"Z" :
    print("the character is an alphabet")
elif ch[0].isdigit():
    print("the character is a digit")
else:
    print("the character is a special character")