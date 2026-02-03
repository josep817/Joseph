year = int(input("Enter a year:"))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(year,"Leap year")
         
        else:
            print(year,"Not aleap year")

    else:
        print(year,"Not aleap year")

else:
    print(year,"Not aleap year")