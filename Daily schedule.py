day=input("Please enter the day : ")
time=input("Please enter the time in 24 hours system : ")
if day=="monday" or day=="tuesday" or day=="wednesday" or day=="thursday" or day=="friday" or day=="saturday":
    if time>="9.00 "and time<"12.30":
        print("Coding Time")
    elif time>="12.30" and time<"14.00":
        print("Lunch break")
    elif time>="14.00" and time<"17.00":
        print("Coding time")
    elif time>="17.00 "and time<"18.00":
        print("Cultural activity")
    elif time>="18.00" and time<"18.30":
        print("Snacks break")
    elif time>="18.30" and time<"20.00":
        print("Coding")
    elif time>="20.00" and time<"21.00":
        print("English activity")
    else:
        print("Free time")
elif day=="sunday":
    print("It's a holiday ! Enjoy your day :) ")
else:
    print("Invalid day or time")        