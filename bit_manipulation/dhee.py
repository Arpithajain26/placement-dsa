"write a logic to check whether it is a leap year"
year=int(input("enter the year"))
if (year%4==0 and year%100!=0) or year%200==0:
    print(f"{year} is leap year")
else:
    print(f"{year} is not leap year")