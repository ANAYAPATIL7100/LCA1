from datetime import date 
#input first date
d1=int(input("Enter day of first date"))
m1=int(input("Enter month of first date"))
y1=int(input("Enter year of first date"))
#input second date
d2=int(input("Enter day of second date"))
m2=int(input("Enter month of second date"))
y2=int(input("Enter year of second date"))
#create date tuples
date1=(y1,m1,d1)
date2=(y2,m2,d2)
#convert tuples into date objects
date_1=date(y1,m1,d1)
date_2=date(y2,m2,d2)
#calculate difference
day=abs((date_2-date_1).days)
print("First date:",date_1)
print("Second date:",date_2)
print("Number of days between the two dates:",day)
