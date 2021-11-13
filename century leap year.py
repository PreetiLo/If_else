year=int(input("Please enter a year : "))
if year %4==0:
  print("The year is a century leap year")
elif year %400==0:
  print("The year is a century leap year")
elif year%100==0:
  print("The year is a century leap year")
else:
    print("The year is not a leap year")                      