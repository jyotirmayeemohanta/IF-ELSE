year=int(input("enter a leap year"))
if year%4==0:
    print(year,"leap year")
elif year%400==0 or year%100==0:
    print(year,"leap year")
else:
    print(year,"not leap year")
