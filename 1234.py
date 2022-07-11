a = int(input("Enter the year: "))

if(a % 400 == 0) and (a % 100 == 0):
    print("{0} is a leap year".format(a))

elif(a % 4 == 0) and (a % 100 != 0):
    print("{0} is a leap year".format(a))
else:
    print("{0} is not a leap year".format(a))
