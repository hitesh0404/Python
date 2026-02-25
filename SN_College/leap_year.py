year = 0
while(year != -1):
    year = input("enter Year")
    year = int(float(year))
    if (year%4==0 and year%100!=0 ) or (year%400==0):
        print(year ," is Leap Year")
    else:
        print(year ,"is Not a leap year")